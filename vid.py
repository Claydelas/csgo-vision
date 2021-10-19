import cv2
import os
import sys
from annotation import annotate_frame


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
    return 0


def video_to_annotated_frames(vid, obj_class):
    count = 0
    stream = cv2.VideoCapture(vid)
    success, image = stream.read()
    while success:
        stream.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
        image, (x, y, w, h) = annotate_frame(image)
        ih, iw, _ = image.shape
        name = f'frames/{os.path.basename(vid).split(".")[0]}-{count}'
        # Save video frame as image
        cv2.imwrite(f'{name}.jpg', image)
        # Save image annotation as YOLO format
        with open(f'{name}.txt', 'w') as f:
            f.write(f'{obj_class} {x/iw} {y/ih} {w/iw} {h/ih}')
        count += 1
        success, image = stream.read()
    return 0


def main():
    if len(sys.argv) > 2:
        try:
            return video_to_annotated_frames(sys.argv[1], sys.argv[2])
        except:
            return "Failed to extract frames from video."
    if len(sys.argv) > 1:
        try:
            return video_to_frames(sys.argv[1])
        except:
            return "Failed to extract frames from video."

    return "Please supply a valid video path as an arg."


if __name__ == '__main__':
    sys.exit(main())
