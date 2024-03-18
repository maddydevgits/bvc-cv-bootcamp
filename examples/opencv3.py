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

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Check for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('madhu.jpg',frame)

# Release the VideoCapture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
