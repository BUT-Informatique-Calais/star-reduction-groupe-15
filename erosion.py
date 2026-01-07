from astropy.io import fits
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

# --- Phase 2 : Réduction localisée avec masque d'étoiles ---
# Open and read the FITS file
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
examples_dir = os.path.join(script_dir, 'examples')

# Prefer explicit file; otherwise pick the first .fits in examples/
fits_candidates = [f for f in os.listdir(examples_dir) if f.lower().endswith('.fits')]
if not fits_candidates:
    raise FileNotFoundError(f'No .fits files found in {examples_dir}')
fits_file = os.path.join(examples_dir, fits_candidates[0])
print(f'Using FITS file: {fits_file}')
hdul = fits.open(fits_file)

# Display information about the file
hdul.info()

# Access the data from the primary HDU
data = hdul[0].data

# Access header information
header = hdul[0].header

# Handle both monochrome and color images
if data.ndim == 3:
    # Color image - need to transpose to (height, width, channels)
    if data.shape[0] == 3:  # If channels are first: (3, height, width)
        data = np.transpose(data, (1, 2, 0))
    # Normalize and save
    data_normalized = (data - data.min()) / (data.max() - data.min())
    plt.imsave('./results/original.png', data_normalized)
    image_uint8 = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')
    image_uint8 = cv.cvtColor(image_uint8, cv.COLOR_RGB2BGR)
else:
    # Monochrome image
    plt.imsave('./results/original.png', data, cmap='gray')
    image_uint8 = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')

# Convert to grayscale for star detection
if image_uint8.ndim == 3:
    gray = cv.cvtColor(image_uint8, cv.COLOR_BGR2GRAY)
else:
    gray = image_uint8

# Pre-filter to reduce noise
gray_blur = cv.medianBlur(gray, 3)

# --- 4.1 Étape A : Création du masque d'étoiles ---
# Use adaptive threshold to detect bright stars
# Parameters (blockSize and C) may be adjusted for other images
block_size = 25  # neighborhood size
C = -5           # bias subtraction
mask = cv.adaptiveThreshold(gray_blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv.THRESH_BINARY, block_size, C)

# Morphological cleanup: remove tiny noise, enlarge stars slightly
kernel_open = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
mask_clean = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel_open, iterations=1)
# Dilate to ensure mask covers star PSF
kernel_dilate = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
mask_dilated = cv.dilate(mask_clean, kernel_dilate, iterations=2)

# Save binary mask
cv.imwrite('./results/star_mask_binary.png', mask_dilated)

# Smooth mask edges with a small Gaussian blur (soft edges)
mask_soft = cv.GaussianBlur(mask_dilated, (11, 11), sigmaX=3)
cv.imwrite('./results/star_mask_soft.png', mask_soft)

# Convert masks to float in [0,1]
M = mask_soft.astype(np.float32) / 255.0

# --- 4.2 Étape B : Réduction localisée ---
# 1) Create an eroded version of the original image
erode_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
eroded_image = cv.erode(image_uint8, erode_kernel, iterations=3)
cv.imwrite('./results/eroded.png', eroded_image)

# 2) Mask M already computed and smoothed above
# Ensure M has same number of channels as image for blending
if image_uint8.ndim == 3:
    M_stack = np.stack([M, M, M], axis=-1)
else:
    M_stack = M

# Convert images to float [0,1] for blending
I_erode = eroded_image.astype(np.float32) / 255.0
I_orig = image_uint8.astype(np.float32) / 255.0

# 3) Interpolation: Ifinal = M * Ierode + (1-M) * Ioriginal
I_final = (M_stack * I_erode) + ((1.0 - M_stack) * I_orig)

# Convert final image back to uint8
I_final_uint8 = np.clip(I_final * 255.0, 0, 255).astype('uint8')
cv.imwrite('./results/final_local_reduction.png', I_final_uint8)

# For grayscale input also save a grayscale final image for convenience
if image_uint8.ndim == 2:
    plt.imsave('./results/final_local_reduction_gray.png', I_final, cmap='gray')

# Close the FITS file
hdul.close()

print('Phase 2 completed: star masks, eroded image, and final blended image saved in ./results/')