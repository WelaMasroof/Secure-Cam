from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO("yolo11n.pt")  # Replace with your model path

# Start capturing video from the webcam (use 0 for default camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Capture frame-by-frameq
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform object detection on the frame
    results = model(frame)

    # Display results on the frame
    annotated_frame = results[0].plot()  # Plot detected objects on the frame

    # Show the frame with detections
    cv2.imshow("YOLO Real-Time Detection", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
