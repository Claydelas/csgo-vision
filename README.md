# Self-learning dataset generation:
```sh
# class 0 for T or 1 for CT
python vid.py --vid ./videos/t_model_0.mp4 --cls 0 --ml True
```
# Train on generated cs:go dataset with:
```sh 
python yolov5/train.py --img 640 --batch 10 --epochs 500 --data dataset.yaml --weights yolov5/yolov5s.pt
```
# Inference:
```sh
python yolov5/detect.py --img 640 --conf 0.2  --weights ./data/weights/best.pt --source ./data/images
```
# Inference on live gameplay (WIP):
```sh
python detect.py
```