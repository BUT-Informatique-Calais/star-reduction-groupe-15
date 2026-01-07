from astropy.io import fits
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

fits_file = './examples/test_M31_linear.fits'
hdul = fits.open(fits_file)

data = hdul[0].data
header = hdul[0].header

if data.ndim == 3:
    if data.shape[0] == 3:
        data = np.transpose(data, (1, 2, 0))
    data_normalized = (data - data.min()) / (data.max() - data.min())
    plt.imsave('./results/original.png', data_normalized)
    image = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
else:
    plt.imsave('./results/original.png', data, cmap='gray')
    image = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) if data.ndim == 3 else image
blurred = cv.GaussianBlur(gray, (5, 5), 0)
mask = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, -3)
cv.imwrite('./results/star_mask.png', mask)


# On mesure les étoiles
contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Différentes catégories d'étoiles en fonction de leur taille
mask_small = np.zeros_like(mask)
mask_medium = np.zeros_like(mask)
mask_large = np.zeros_like(mask)

for cnt in contours:
    area = cv.contourArea(cnt)
    if area < 5:
        continue
    
    if area < 50:
        cv.drawContours(mask_small, [cnt], -1, 255, -1)
    elif area < 200:
        cv.drawContours(mask_medium, [cnt], -1, 255, -1)
    else:
        cv.drawContours(mask_large, [cnt], -1, 255, -1)

# L'érosion est différente pour chacune des catégories pour adapter au mieux et être plus précis
kernel_small = np.ones((3, 3), np.uint8)
kernel_medium = np.ones((5, 5), np.uint8)
kernel_large = np.ones((7, 7), np.uint8)

eroded_small = cv.erode(image, kernel_small, iterations=1)
eroded_medium = cv.erode(image, kernel_medium, iterations=1)
eroded_large = cv.erode(image, kernel_large, iterations=1)

# On combine tout les résultats pour obtenir notre image finale
result = image.copy()

m_small = cv.GaussianBlur(mask_small, (5, 5), 0).astype(np.float32) / 255.0
m_medium = cv.GaussianBlur(mask_medium, (5, 5), 0).astype(np.float32) / 255.0
m_large = cv.GaussianBlur(mask_large, (5, 5), 0).astype(np.float32) / 255.0

if data.ndim == 3:
    m_small = m_small[:, :, np.newaxis]
    m_medium = m_medium[:, :, np.newaxis]
    m_large = m_large[:, :, np.newaxis]

# Appliquer les erosions

result = (m_small * eroded_small + (1 - m_small) * result).astype(np.uint8)
result = (m_medium * eroded_medium + (1 - m_medium) * result).astype(np.uint8)
result = (m_large * eroded_large + (1 - m_large) * result).astype(np.uint8)

cv.imwrite('./results/eroded.png', result)
cv.imwrite('./results/final.png', result)

hdul.close()