import cv2
import os
import sys
from annotation import annotate_frame
from pathlib import Path
import torch
import argparse

Path('data/images').mkdir(parents=True, exist_ok=True)
Path('data/labels').mkdir(parents=True, exist_ok=True)


def video_to_frames(vid):
    count = 0
    stream = cv2.VideoCapture(vid)
    success, image = stream.read()
    while success:
        stream.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
        cv2.imwrite(
            f'data/images/{os.path.basename(vid).split(".")[0]}-{count}.jpg', image)
        count += 1
        success, image = stream.read()
    return 0


def video_to_annotated_frames(vid, obj_class):
    count = 0
    stream = cv2.VideoCapture(vid)
    success, image = stream.read()
    while success:
        stream.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
        x, y, w, h = annotate_frame(image)
        ih, iw, _ = image.shape
        name = f'{os.path.basename(vid).split(".")[0]}-{count}'
        # Save video frame as image
        cv2.imwrite(f'data/images/{name}.jpg', image)
        # Save image annotation as YOLO format
        with open(f'data/labels/{name}.txt', 'w') as f:
            f.write(f'{obj_class} {(x + w/2)/iw} {(y + h/2)/ih} {w/iw} {h/ih}')
        count += 1
        success, image = stream.read()
    return 0

    
def video_to_annotated_frames_ml(vid, obj_class):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5m')
    model.conf = 0.5
    model.classes = [0]
    count = 0
    stream = cv2.VideoCapture(vid)
    success, image = stream.read()
    while success:
        stream.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
        name = f'{os.path.basename(vid).split(".")[0]}-{count}'
        # Save video frame as image
        cv2.imwrite(f'data/images/{name}.jpg', image)

        # Save image annotation as YOLO format
        boxes = model(image[:,:,::-1]).xywhn[0]
        with open(f'data/labels/{name}.txt', 'w') as f: 
            f.write("\n".join([f'{obj_class} {box[0]} {box[1]} {box[2]} {box[3]}' for box in boxes]))
        count += 1
        success, image = stream.read()
    return 0


def main(opt):
    if 'cls' in opt:
        if opt.ml:
            return video_to_annotated_frames_ml(opt.vid, opt.cls)
        else:
            return video_to_annotated_frames(opt.vid, opt.cls)
    return video_to_frames(opt.vid)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--vid', type=str, required=True, help='path to video file')
    parser.add_argument('--cls', type=int, help='class: 0 - T, 1 - CT')
    parser.add_argument('--ml', type=bool, help='whether to use machine learning for data generation')
    opt = parser.parse_args()
    sys.exit(main(opt))
