# Self-learning dataset generation:
```py
python vid.py ./videos/t_model_0.mp4 0 # class 0 for T or 1 for CT
```
# Train on generated cs:go dataset with:
```py 
python yolov5/train.py --img 640 --batch 10 --epochs 500 --data dataset.yaml --weights yolov5/yolov5s.pt
```
# Inference:
```py
python yolov5/detect.py --img 640 --conf 0.2  --weights ./data/weights/best.pt --source ./data/images
```
# Inference on live gameplay (WIP):
```py
python detect.py
```