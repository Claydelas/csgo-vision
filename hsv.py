import cv2
import numpy as np
import sys
from functools import partial


def hsv(img: str):
    # Load image
    image = cv2.imread(img)

    # Create a window
    cv2.namedWindow('image')

    # Initialise default HSV values
    vals = {"HMin": 0, "SMin": 0, "VMin": 0, "HMax": 179, "SMax":255, "VMax": 255}

    def onChange(key, new):
        # Change HSV val to the new value
        vals[key] = new
        # Re-draw image
        draw()

    def draw():
        # Get current positions of all trackbars
        hMin = vals['HMin']
        sMin = vals['SMin']
        vMin = vals['VMin']
        hMax = vals['HMax']
        sMax = vals['SMax']
        vMax = vals['VMax']

        # Set minimum and maximum HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

        # Convert to HSV format and color threshold
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)

        print(f'(hMin = {hMin} , sMin = {sMin}, vMin = {vMin}), (hMax = {hMax} , sMax = {sMax}, vMax = {vMax})')
        
        # Display result image
        cv2.imshow('image', result)

    # Create trackbars for color change
    # Hue is from 0-179 for Opencv
    cv2.createTrackbar('HMin', 'image', 0, 179, partial(onChange,"HMin"))
    cv2.createTrackbar('SMin', 'image', 0, 255, partial(onChange,"SMin"))
    cv2.createTrackbar('VMin', 'image', 0, 255, partial(onChange,"VMin"))
    cv2.createTrackbar('HMax', 'image', 179, 179, partial(onChange,"HMax"))
    cv2.createTrackbar('SMax', 'image', 255, 255, partial(onChange,"SMax"))
    cv2.createTrackbar('VMax', 'image', 255, 255, partial(onChange,"VMax"))

    # Spawn GUI
    draw()
    while not (cv2.waitKey(25) & 0xFF == ord("q")):
        pass

    # Cleanup
    cv2.destroyAllWindows()
    return 0


def main():
    if len(sys.argv) > 1:
        try:
            return hsv(sys.argv[1])
        except:
            return "Image path not valid."
    return "Please supply a valid image path as an arg."


if __name__ == '__main__':
    sys.exit(main())
