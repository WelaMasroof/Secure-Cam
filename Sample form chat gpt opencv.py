import cv2

# Initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open a video capture from the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read frames from the video capture
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize frame to improve processing speed and accuracy
    frame = cv2.resize(frame, (640, 480))

    # Detect people in the frame
    (rects, _) = hog.detectMultiScale(frame, 
                                      winStride=(8, 8),
                                      padding=(8, 8), 
                                      scale=1.05)
    
    # Draw bounding boxes for each detected person
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the output frame
    cv2.imshow("Real-Time Human Detection", frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
