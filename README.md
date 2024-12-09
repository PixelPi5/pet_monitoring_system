# Pet Monitoring System using YOLOv8

## Overview
This project implements a pet activity monitoring system using YOLOv8 object detection, designed to classify and notify five pet behaviors: **eating**, **playing**, **sleeping**, **stretching**, and **walking**. The system utilizes data augmentation to enhance model performance and deploys the trained model on a Raspberry Pi for real-time notifications via Telegram.

---

## Features
- **YOLOv8 Object Detection**: Detects and classifies pet activities.
- **Data Augmentation**: Boosts model accuracy and generalization.
- **Real-Time Telegram Notifications**: Alerts for detected activities.
- **Raspberry Pi Deployment**: Optimized for edge device inference.

---

## Project Workflow

### 1. Dataset Preparation
1. **Data Collection**:
   - Created a dataset with 5 classes: **eating**, **playing**, **sleeping**, **stretching**, and **walking**.
   - Each class initially contained 80 training images and 20 validation images, except for **walking**, which was later equalized.

2. **Data Augmentation**:
   - Used Albumentations to augment training images with techniques like flipping, rotation, brightness adjustment, and scaling.
   - Increased the training dataset size to 320 images per class.

---

### 2. Model Training
1. **YOLOv8 Model Selection**:
   - Used YOLOv8 Nano (`yolov8n.pt`) for lightweight and efficient training.

2. **Training Command**:
   - Ran the following command to train the model for 50 epochs with 640x640 resolution:
     ```bash
     yolo train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640 batch=8
     ```

3. **Validation**:
   - Validated the trained model to ensure proper detection of all 5 activities.

---

### 3. Inference and Notifications
1. **Real-Time Inference**:
   - Implemented `run_inference_with_notifications.py` to process live video feeds and send Telegram alerts when specific activities are detected.

2. **Testing on Video**:
   - Used `testing_video.py` to test the model on pre-recorded videos for accuracy.

---

## Directory Structure
PetMonitoringSystem/
│
├── dataset/                 # Original dataset (training and validation images/labels)
├── dataset_augmented/       # Augmented dataset (if applicable)
├── runs/                    # YOLO training results
├── venv-python3.10/         # Virtual environment (do NOT upload this to GitHub)
├── scripts/                 # Python scripts
│   ├── augment.py           # Augmentation script
│   ├── run_inference_with_notifications.py # Inference script with Telegram notifications
│   ├── testing_video.py     # Video testing script
│   ├── cat_walking_images.py # Helper script for downloading images
├── cat_activity.mp4         # Sample video for testing (optional)
├── models/                  # YOLO models
│   ├── yolov8n.pt           # YOLO Nano model
│   ├── yolov8s.pt           # YOLO Small model
│   ├── yolov11n.pt          # Custom-trained model (rename after training)
├── data.yaml                # YOLO dataset configuration
├── README.md                # Documentation for the project
├── .gitignore               # Specify files/folders to ignore (e.g., venv and runs)


---

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/PetMonitoringSystem.git
cd PetMonitoringSystem

### 2. Create a Virtual Environment
```bash
python3.10 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
```bash
pip install -r requirements.txt

### 4. Training the Model
```bash
yolo train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640 batch=8

### 5. Testing the model
```bash
python scripts/testing_video.py

### 6. Running Inference with Telegram Notifications
```bash
python scripts/run_inference_with_notifications.py

### 7. Deploying on Raspberry Pi
Transfer Files to Raspberry Pi: Use scp to copy the required files:
```bash
scp -r PetMonitoringSystem botagozmaya@172.30.1.55:/home/botagozmaya/

Install Dependencies on Raspberry Pi: Access the Raspberry Pi via SSH and activate the virtual environment:
```bash
ssh botagozmaya@172.30.1.55
cd /home/botagozmaya/PetMonitoringSystem
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configure Raspberry Pi: Ensure that your Raspberry Pi has a connected camera and required drivers enabled:
```bash
sudo raspi-config

Run Inference on Raspberry Pi: Execute the inference script on the Raspberry Pi:
```bash
python scripts/run_inference_with_notifications.py

