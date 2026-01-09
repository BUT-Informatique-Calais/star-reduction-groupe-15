import cv2 as cv
import numpy as np
from astropy.io import fits
import requests, json
from PIL import Image
import os

class AstroPictureHandler:
    @staticmethod
    def process_reduction(fits_file: str, kernel_size: tuple[int, int], blur_size: tuple[int, int], iters: int, threshold_val: int):
        try:
            hdul = fits.open(fits_file)
            data = hdul[0].data
            hdul.close()

            if data is None: return None

            # normalisation et gestion couleur/mono
            if data.ndim == 3:
                if data.shape[0] == 3:
                    data = np.transpose(data, (1, 2, 0))
                image = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')
                # OpenCV déjà en BGR
            else:
                image = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')

            # création du masque (Phase 2)
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) if data.ndim == 3 else image
            # sécurité : blur_size doit être impair
            blurred = cv.GaussianBlur(gray, blur_size, 0)
            mask = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, threshold_val)

            #érosion et Blending
            kernel = np.ones(kernel_size, np.uint8)
            eroded_image = cv.erode(image, kernel, iterations=iters)

            mask_smooth = cv.GaussianBlur(mask, blur_size, 0)
            M = mask_smooth.astype(np.float32) / 255.0

            if data.ndim == 3:
                M = M[:, :, np.newaxis]
            
            #calcul final
            final_image = (M * eroded_image + (1 - M) * image).astype(np.uint8)

            # on renvoie l'image finale
            return final_image
        except Exception as e:
            print(f"Erreur calcul : {e}")
            return None
        
    @staticmethod
    def getPictures() -> list:
        return [os.path.join(os.path.dirname(__file__), "..", "examples", f) for f in os.listdir(os.path.join(os.path.dirname(__file__), "..", "examples"))]
            
    @staticmethod
    def convert_to_fits(image_path, output_fits_path):
        
        img = Image.open(image_path).convert('L')
        
        data = np.array(img)
        
        hdu = fits.PrimaryHDU(data)
        
        hdu.header['OBJECT'] = 'M101-SIMULATED'
        hdu.header['INSTRUME'] = 'PIL-CONVERTER'
        
        hdu.writeto(output_fits_path, overwrite=True)