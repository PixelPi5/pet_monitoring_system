import cv2
from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO("runs/detect/train/weights/best.pt")  # Path to your best.pt model

# Load the video file
video_path = "cat_video.mp4"  # Replace with the name of your recorded video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Unable to open video {video_path}")
    exit()

# Loop through video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video or error in reading frames.")
        break

    # Perform inference
    results = model.predict(source=frame, save=False, conf=0.5, imgsz=1280)

    # Visualize the results
    annotated_frame = results[0].plot()  # Draw bounding boxes on the frame
    cv2.imshow("YOLO Inference", annotated_frame)

    # Example: Process detections for notifications
    for r in results:
        for box in r.boxes:
            cls = box.cls.cpu().numpy()[0]  # Get class index
            if cls == 0:  # Assuming 'cat' class is 0
                print("Cat detected: Sending notification for activity...")

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
