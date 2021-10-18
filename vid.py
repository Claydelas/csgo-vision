import cv2
import os


def video_to_frames(vid):
    count = 0
    stream = cv2.VideoCapture(vid)
    success, image = stream.read()
    while success:
        stream.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
        cv2.imwrite(
            f'frames/{os.path.basename(vid).split(".")[0]}-{count}.jpg', image)
        count += 1
        success, image = stream.read()
