import cv2
import mss
import numpy
from model import detect

with mss.mss() as sct:
    while True:
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(sct.monitors[0]))

        # Placeholder
        detections = detect(img)

        # Display the detections
        cv2.imshow("OpenCV/Numpy normal", detections)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break