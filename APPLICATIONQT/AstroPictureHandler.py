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

            # 1. Normalisation
            if data.ndim == 3:
                # Si FITS est (C, H, W), on passe en (H, W, C)
                if data.shape[0] == 3:
                    data = np.transpose(data, (1, 2, 0))
                image_rgb = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')
            else:
                image_rgb = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')

            # --- SAUVEGARDE DE L'ORIGINALE ---
            results_dir = os.path.join(os.path.dirname(__file__), "..", "results")
            os.makedirs(results_dir, exist_ok=True)
            
            # Pour cv.imwrite, il FAUT du BGR si l'image est en couleur
            if data.ndim == 3:
                image_bgr = cv.cvtColor(image_rgb, cv.COLOR_RGB2BGR)
                cv.imwrite(os.path.join(results_dir, "original.png"), image_bgr)
            else:
                cv.imwrite(os.path.join(results_dir, "original.png"), image_rgb)
            # ---------------------------------

            # 2. Préparation pour le traitement OpenCV (Travail en niveaux de gris pour le masque)
            # On utilise image_rgb car cv.cvtColor(RGB2GRAY) est standard
            gray = cv.cvtColor(image_rgb, cv.COLOR_RGB2GRAY) if data.ndim == 3 else image_rgb
            blurred = cv.GaussianBlur(gray, blur_size, 0)
            mask = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, threshold_val)

            # 3. Érosion et Blending
            kernel = np.ones(kernel_size, np.uint8)
            eroded_image = cv.erode(image_rgb, kernel, iterations=iters)

            mask_smooth = cv.GaussianBlur(mask, blur_size, 0)
            M = mask_smooth.astype(np.float32) / 255.0

            if data.ndim == 3:
                M = M[:, :, np.newaxis]
            
            # Calcul final (préserve le format RGB de départ)
            final_image = (M * eroded_image + (1 - M) * image_rgb).astype(np.uint8)

            return final_image
            
        except Exception as e:
            print(f"Erreur calcul : {e}")
            return None
        
    @staticmethod
    def getPictures() -> list:
        return [os.path.join(os.path.dirname(__file__), "..", "examples", f) for f in os.listdir(os.path.join(os.path.dirname(__file__), "..", "examples"))]
            