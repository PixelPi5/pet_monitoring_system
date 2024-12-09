import cv2
import time
import telebot
from ultralytics import YOLO

print("Starting the script...")

# Telegram bot credentials
BOT_API_TOKEN = "7898895797:AAF_1ii76w0ZHW2n0Xbdsq0mvFuGN66Tz_0"  # Replace with your actual bot token
CHAT_ID = "859428685"  # Replace with your chat ID
bot = telebot.TeleBot(BOT_API_TOKEN)

# Load the trained YOLO model
print("Loading model...")
model = YOLO('/home/botagozmaya/project-folder/runs/detect/train9/weights/best.pt')  # Adjust path as needed
print("Model loaded successfully.")

# Define action-to-notification mapping
actions = {
    "cat_eating": "The cat is eating the food",
    "cat_sleeping": "The cat is sleeping on the bed",
    "cat_walking": "The cat is walking in the room",
    "cat_stretching": "The cat is stretching",
    "cat_playing": "The cat is playing with the toy",
}

# Video file path
video_path = '/home/botagozmaya/project-folder/cat_activity.mp4'  # Replace with the path to your video file
cap = cv2.VideoCapture(video_path)

# Variables to track notifications
last_action = None  # Tracks the last action detected
cat_last_seen_time = time.time()
cat_absence_threshold = 30  # 5 minutes in seconds
cat_present = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video or read error.")
        break

    # Run YOLO detection on the frame
    results = model(frame)
    detections = results[0].boxes  # Get the detected boxes

    current_time = time.time()
    detected_classes = []

    if detections:
        for box in detections:
            class_name = model.model.names[int(box.cls)]  # Access class names correctly
            confidence = float(box.conf)  # Confidence score of the detection

            # Filter detections with low confidence
            if confidence < 0.5:
                continue

            detected_classes.append(class_name)

            # Handle notifications for new actions
            if class_name in actions and class_name != last_action:
                notification = actions[class_name]
                bot.send_message(CHAT_ID, notification)
                last_action = class_name

        cat_last_seen_time = current_time
        if not cat_present:
            bot.send_message(CHAT_ID, "The cat is detected in the room, you may not worry.")
            cat_present = True
    else:
        if cat_present and current_time - cat_last_seen_time > cat_absence_threshold:
            bot.send_message(CHAT_ID, "The cat is not in the room.")
            cat_present = False
            last_action = None  # Reset last action when the cat leaves

    # Display the frame for debugging purposes
   # Remove or modify the part causing the SyntaxError
    if hasattr(cv2, 'imshow'):
        cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()




