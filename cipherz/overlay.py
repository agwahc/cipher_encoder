import numpy as np
import cv2
import dir

canvas = np.ones([500, 500, 3], 'uint8') * 255

# extract barcode from fill_tmp.png using contours
img = cv2.imread(dir.fill_tmp_png(), 1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 115, 1)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Draw command
image = np.ones([img.shape[0], img.shape[1], 3], 'uint8')*255
color = (0, 0, 0)

cv2.drawContours(image, contours, -1, color, 3/10)
cv2.imshow('Original', img)
cv2.imshow('Contours', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
