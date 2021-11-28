import numpy as np
import cv2

def annotate_frame(img):
    # Convert sample to HSV color space
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # (hMin = 40 , sMin = 25, vMin = 100), (hMax = 179 , sMax = 255, vMax = 255)
    # Create a range mask for the color of bounding boxes found in samples
    mask = cv2.inRange(imghsv, np.array([40, 25, 100]), np.array([179, 255, 255]))

    # Retrieve all contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    bbox = contours[np.argmax(areas)]

    # Draw the largest contour (the contour that best approximates the bounding box in the sample)
    # x, y, w, h = cv2.boundingRect(bbox)
    # cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    return cv2.boundingRect(bbox)