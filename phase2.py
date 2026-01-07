from astropy.io import fits
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


# Open and read the FITS file
fits_file = './examples/test_M31_linear.fits'
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
        
    # If already (height, width, 3), no change needed
    # Normalize the entire image to [0, 1] for matplotlib
    data_normalized = (data - data.min()) / (data.max() - data.min())
    
    # Save the data as a png image (no cmap for color images)
    plt.imsave('./results/original.png', data_normalized)
    image = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    # Il faut passer en BGR car les rouges se changent en bleu en RGB,
    # la ligne du dessus sert à inverser ces couleurs. 
else:
    # Monochrome image
    plt.imsave('./results/original.png', data, cmap='gray')
    # Convert to uint8 for OpenCV
    image = ((data - data.min()) / (data.max() - data.min()) * 255).astype('uint8')

# Création du masque
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) if data.ndim == 3 else image
blurred = cv.GaussianBlur(gray, (5, 5), 0)
mask = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, -5)
cv.imwrite('./results/star_mask.png', mask)

# Define a kernel for erosion
kernel = np.ones((3,3), np.uint8)

# Perform erosion
eroded_image = cv.erode(image, kernel, iterations=1)

# Save the eroded image 
cv.imwrite('./results/eroded.png', eroded_image)

mask_smooth = cv.GaussianBlur(mask, (5, 5), 0)
M = mask_smooth.astype(np.float32) / 255.0

# I_final = (M * I_erode) + ((1 - M) * I_original)
if data.ndim == 3:
    M = M[:, :, np.newaxis]
final_image = (M * eroded_image + (1 - M) * image).astype(np.uint8)

cv.imwrite('./results/final.png', final_image)

# Close the file
hdul.close()
