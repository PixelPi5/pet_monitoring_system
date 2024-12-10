# Pet Monitoring System using YOLOv8

## Overview
This project implements a pet activity monitoring system using YOLOv8 object detection, designed to classify and notify five pet behaviors: **eating**, **playing**, **sleeping**, **stretching**, and **walking**. The system utilizes data augmentation to enhance model performance and deploys the trained model on a Raspberry Pi for real-time notifications via Telegram.

---
## Table of Contents
1. Features
2. Directory Structure
3. Installation
4. Usage
5. Results
6. Deploying on Raspberry Pi
7. Contributing
8. License

## Features
- **Real-time Pet Monitoring**: Detects pet behaviors such as eating, sleeping, walking, playing, and stretching.
- **Notifications**: Sends updates to Telegram when specific behaviors are detected.
- **Customizable Model**: Fine-tuned YOLOv8 model for accurate detection.
- **Support for Raspberry Pi**: Lightweight implementation tailored for edge devices.
- **Training Pipeline**: Custom dataset preparation and augmentation for YOLOv8 training.

---

## Project Workflow

## Directory Structure
```bash
PetMonitoringSystem/
├── dataset/                 # Original dataset (training and validation images/labels)
├── dataset_augmented/       # Augmented dataset (if applicable)
├── runs/                    # YOLO training results
├── venv-python3.10/         # Virtual environment (do NOT upload this to GitHub)
├── scripts/                 # Python scripts
│   ├── augment.py           # Augmentation script
│   ├── run_inference_with_notifications.py  # Inference script with Telegram notifications
│   ├── testing_video.py     # Video testing script
│   ├── cat_walking_images.py # Helper script for downloading images
├── cat_activity.mp4         # Sample video for testing (optional)
├── models/                  # YOLO models
│   ├── yolov8n.pt           # YOLO Nano model
│   ├── yolov11n.pt          # Custom-trained model (rename after training)
├── data.yaml                # YOLO dataset configuration
├── README.md                # Documentation for the project
├── .gitignore               # Specify files/folders to ignore (e.g., venv and runs)

---

---

## Installation
1. Clone the Repository
```bash
git clone https://github.com/PixelPi5/pet_monitoring_system.git
cd pet_monitoring_system

2. Create a Virtual Environment
```bash
python3 -m venv venv-python3.10
source venv-python3.10/bin/activate

3. Install Dependencies
```bash
pip install -r requirements.txt

4. Prepare the dataset:
Place your training and validation images in dataset/train and dataset/valid, respectively.
Ensure labels are in YOLO format.

5. Update the data.yaml file with your dataset paths.

## Usage
1. Training
Train the YOLOv8 model using your prepared dataset:
```bash
yolo train model=yolov8n.pt data=data.yaml epochs=50 imgsz=1280 batch=8

2. Testing
```bash
Run inference on a sample video:
python run_inference_with_notifications.py

3. Deployment
Deploy the system on Raspberry Pi for real-time monitoring.

## Results
| **Behavior**   | **Precision** | **Recall** | **mAP50** | **mAP50-95** |
|----------------|---------------|------------|-----------|--------------|
| Eating         | 91.4%        | 100%       | 99.5%     | 66.5%        |
| Playing        | 59.4%        | 80.0%      | 70.6%     | 45.9%        |
| Sleeping       | 55.9%        | 50.0%      | 66.7%     | 28.9%        |
| Stretching     | 64.9%        | 70.0%      | 59.3%     | 35.2%        |
| Walking        | 95.2%        | 75.0%      | 87.7%     | 53.2%        |


## Deploying on Raspberry Pi
1. Transfer Files to Raspberry Pi: 
```bash
scp -r PetMonitoringSystem botagozmaya@172.30.1.55:/home/botagozmaya/

2. Install Dependencies on Raspberry Pi
Access the Raspberry Pi via SSH and activate the virtual environment:
```bash
ssh botagozmaya@172.30.1.55
cd /home/botagozmaya/PetMonitoringSystem
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Configure Raspberry Pi: 
```bash
sudo raspi-config

4. Run Inference on Raspberry Pi: 
```bash
python scripts/run_inference_with_notifications.py

## Contributing
Feel free to submit issues or pull requests to improve this project. Contributions are welcome!

## License
This project is licensed under the MIT License.

