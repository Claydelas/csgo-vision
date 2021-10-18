import numpy as np
import cv2

# Open sample
img = cv2.imread("1.png")

# Convert sample to HSV color space
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# (hMin = 4 , sMin = 87, vMin = 191), (hMax = 12 , sMax = 255, vMax = 255)
lower = np.array([4, 87, 191])
upper = np.array([12, 255, 255])

# Create a range mask for the color of bounding boxes found in samples
mask = cv2.inRange(imghsv, lower, upper)

# Retrieve all contours
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour
areas = [cv2.contourArea(c) for c in contours]
bbox = contours[np.argmax(areas)]

# Draw the largest contour (the contour that best approximates the bounding box in the sample)
x, y, w, h = cv2.boundingRect(bbox)
cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
cv2.imshow("sample", img)

cv2.waitKey(0)