# uav-mobfinder (Osprey)
Application For Drone Controller Module to Localize and Navigate Drone to Man-Over-Board Victim. Operates as a vision guided companion computer for autonomous flight control over low latency MAVLink communication to ArduPilot flight controller

## Listen
When landed, the device is placed on deck, listening for asychronous MOB (Man-Overboard) messages arriving from the submersion module over ESP-NOW link. When a MOB packet arrives, the victim GPS coordinates are used as the first waypoint to approach during the start of the search mission. If GPS coordinates are not present, a predefined mission will be used as a baseline.

## Launch
The companion computer will connect to the flight controller over physical serial link. Once ready to be armed, Operating in a guided mode, the UAV will be launched to a given altitude. An optimal altitude is between 20 and 50 meters above sea level, because this is the best altitude our YOLO models are trained on. While waiting for the approach to this altitude, the RGB YOLO model will be loaded. We can now either approach (simple_goto) a relative GPS location or begin a preloaded mission.

## Mission



## Run YOLOv7 Inference (Thermal or RGB)
The models we have are currently not optimized with TensorRT framework. The best.pts models for thermal and RGB trained PyTorch models can be downloaded from our internal google drive and placed within MOBDrone-YOLOv7 submodules.

### To Invoke Inference
```
$ python3 MOBDrone-YOLOv7/detect.py --weights <relative-path-to-best-pts.pt> --conf 0.1 --source {dataset.location}/test/images
```