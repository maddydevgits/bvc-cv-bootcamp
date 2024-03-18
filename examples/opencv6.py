import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera, you can change it if you have multiple cameras

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Read and display frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    # Draw a rectangle on the frame
    pt1 = (50, 50)  # Top-left corner of the rectangle
    pt2 = (200, 200)  # Bottom-right corner of the rectangle
    color = (0, 255, 0)  # BGR color (Green)
    thickness = 2
    cv2.rectangle(frame, pt1, pt2, color, thickness)

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Check for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
