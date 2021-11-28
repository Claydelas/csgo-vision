import cv2
import mss
import numpy
import torch
import atexit
from pathlib import Path

Path('out').mkdir(exist_ok=True)

# This would need another, body part segmentation pass,
# to figure out the position of the player model's head
def detect(model, img):
    res = model(img)
    # draw detection boxes
    ims = res.render()
    return ims[0]

with mss.mss() as sct:
    model = torch.hub.load('./yolov5', 'custom', path='./data/weights/best.pt', source='local')
    # TODO: Replace VideoWriter in prod
    # Instead of saving an annotated video, this should instead calculate the the offset of
    # the bounding box in regards to the middle of the frame and adjust the mouse
    vid_writer = cv2.VideoWriter('./out/detections.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (1920, 1080))
    atexit.register(vid_writer.release)
    while True:
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(sct.monitors[0]))
        detections = detect(model, img)
        vid_writer.write(detections)