# uav-mobfinder
Application For Drone Controller Module to Localize and Navigate Drone to Man-Over-Board Victim


## Run YOLOv7 Inference (Thermal or RGB)
The models we have are currently not optimized with TensorRT framework. The best.pts models for thermal and RGB trained PyTorch models can be downloaded from our internal google drive and placed within MOBDrone-YOLOv7 submodules.

### To Invoke Inference
```
$ python3 MOBDrone-YOLOv7/detect.py --weights <relative-path-to-best-pts.pt> --conf 0.1 --source {dataset.location}/test/images
```