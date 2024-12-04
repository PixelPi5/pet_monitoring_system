Pet Monitoring System Using YOLO and Telegram Notifications

Overview

This project focuses on creating an AI-based pet monitoring system using YOLOv8 for object detection and action recognition. The system detects specific activities of a cat (eating, sleeping, playing, stretching, walking) from input videos and sends notifications via Telegram when these actions are recognized.

Features

YOLOv8-Based Action Recognition:
Detects and classifies the following cat actions: eating, sleeping, playing, stretching, and walking.
Telegram Integration:
Sends real-time notifications to a Telegram bot when specific cat actions are detected.
Video Analysis:
Processes input videos to identify and classify cat behaviors.

Project Structure
PetMonitoringSystem/
│
├── dataset/                     # Custom dataset for training YOLOv8
│   ├── images/                  # Training and validation images
│   ├── labels/                  # Corresponding YOLOv8 annotation files
│   └── data.yaml                # YOLO dataset configuration file
│
├── runs/                        # YOLO training results
│   ├── detect/                  # Detection output folders
│   └── train/                   # Training result folders (e.g., train9/best.pt)
│
├── telegram_bot/                # Telegram bot integration
│   └── notify.py                # Python script to send notifications via Telegram
│
├── video_input/                 # Input videos for testing
│   └── sample_video.mp4         # Sample video file (to be analyzed)
│
├── requirements.txt             # Required Python libraries
├── train_model.py               # YOLOv8 training script
├── detect_actions.py            # YOLOv8 detection script
└── README.md                    # Project documentation


Steps Completed

1. Dataset Preparation
Created a labeled dataset of cat actions for YOLOv8.
Organized the dataset into:
images/: Contains the training and validation images.
labels/: YOLO annotation files for bounding boxes and classes.
Configured the data.yaml file:
train: dataset/images/train
val: dataset/images/val
nc: 5  # Number of classes
names: ['eating', 'sleeping', 'playing', 'stretching', 'walking']


2. YOLOv8 Training
Trained YOLOv8 using the following command:
yolo task=detect mode=train model=yolov8s.pt data=dataset/data.yaml epochs=50 imgsz=1280

Resulting weights saved in the runs/train9/ folder:
best.pt: Best model checkpoint.
last.pt: Final model checkpoint.

3. YOLOv8 Inference
Created a script to perform inference on input videos (detect_actions.py).
Detection output includes bounding boxes and class labels for cat actions.
Command to run the script:
python detect_actions.py --weights runs/train9/best.pt --source video_input/sample_video.mp4

4. Telegram Notifications
Integrated Telegram bot for real-time notifications of detected cat actions.
Steps to Set Up Telegram Bot:
Created a bot using BotFather and obtained the API_TOKEN.
Retrieved the chat_id to send notifications.
Developed the notify.py script to send notifications.
Example notification logic:
if action == "eating":
    send_notification("Your cat is eating!")
elif action == "sleeping":
    send_notification("Your cat is sleeping!")


Usage Instructions

1. Install Dependencies
Install required Python libraries:
pip install -r requirements.txt

2. Train the Model
Use YOLOv8 to train the model on your dataset:
yolo task=detect mode=train model=yolov8s.pt data=dataset/data.yaml epochs=50 imgsz=1280

3. Run Inference
Analyze input videos using the trained model:
python detect_actions.py --weights runs/train9/best.pt --source video_input/sample_video.mp4

4. Telegram Notifications
Ensure the API_TOKEN and chat_id are correctly configured in the notify.py script:
TELEGRAM_API_TOKEN = '7898895797:AAF_1ii76w0ZHW2n0Xbdsq0mvFuGN66Tz_0'
CHAT_ID = '859428685'

Run the notification script during inference to receive updates:
python telegram_bot/notify.py


Next Steps
Deploy the trained model on Raspberry Pi for real-time video analysis.
Optimize the Telegram notification system for seamless integration.

Requirements
Python 3.8+
YOLOv8
Telegram Bot API
OpenCV
PyTorch
Install all dependencies using the provided requirements.txt file.
