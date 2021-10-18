import numpy as np
import cv2

def interpolate_frame(img):
    # Convert sample to HSV color space
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # More lenient mask for bound box color
    mask = cv2.inRange(imghsv, np.array([0, 67, 175]), np.array([12, 255, 255]))
    # Replace original bbox with interpolated pixels
    img = cv2.inpaint(img, mask, 2, cv2.INPAINT_TELEA)

    return img

def annotate_frame(img):
    # Convert sample to HSV color space
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # (hMin = 4 , sMin = 87, vMin = 191), (hMax = 12 , sMax = 255, vMax = 255)
    # Create a range mask for the color of bounding boxes found in samples
    mask = cv2.inRange(imghsv, np.array([4, 87, 191]), np.array([12, 255, 255]))

    # Retrieve all contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    bbox = contours[np.argmax(areas)]

    return (img, cv2.boundingRect(bbox))
