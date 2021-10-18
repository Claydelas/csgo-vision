import cv2
import numpy as np
import sys


def __skip__(x):
    pass


def hsv(img: str):
    # Load image
    image = cv2.imread(img)

    # Create a window
    cv2.namedWindow('image')

    # Create trackbars for color change
    # Hue is from 0-179 for Opencv
    cv2.createTrackbar('HMin', 'image', 0, 179, __skip__)
    cv2.createTrackbar('SMin', 'image', 0, 255, __skip__)
    cv2.createTrackbar('VMin', 'image', 0, 255, __skip__)
    cv2.createTrackbar('HMax', 'image', 0, 179, __skip__)
    cv2.createTrackbar('SMax', 'image', 0, 255, __skip__)
    cv2.createTrackbar('VMax', 'image', 0, 255, __skip__)

    # Set default value for Max HSV trackbars
    cv2.setTrackbarPos('HMax', 'image', 179)
    cv2.setTrackbarPos('SMax', 'image', 255)
    cv2.setTrackbarPos('VMax', 'image', 255)

    # Initialize HSV min/max values
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0

    while(True):
        # Get current positions of all trackbars
        hMin = cv2.getTrackbarPos('HMin', 'image')
        sMin = cv2.getTrackbarPos('SMin', 'image')
        vMin = cv2.getTrackbarPos('VMin', 'image')
        hMax = cv2.getTrackbarPos('HMax', 'image')
        sMax = cv2.getTrackbarPos('SMax', 'image')
        vMax = cv2.getTrackbarPos('VMax', 'image')

        # Set minimum and maximum HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

        # Convert to HSV format and color threshold
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)

        # Print if there is a change in HSV value
        if phMin != hMin | psMin != sMin | pvMin != vMin | phMax != hMax | psMax != sMax | pvMax != vMax:
            print(
                f'(hMin = {hMin} , sMin = {sMin}, vMin = {vMin}), (hMax = {hMax} , sMax = {sMax}, vMax = {vMax})')
            phMin = hMin
            psMin = sMin
            pvMin = vMin
            phMax = hMax
            psMax = sMax
            pvMax = vMax

        # Display result image
        cv2.imshow('image', result)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

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
