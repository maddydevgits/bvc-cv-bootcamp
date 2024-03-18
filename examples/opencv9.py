import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera, you can change it if you have multiple cameras

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    # Perform skin color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 48, 80], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize the contour area
    contour_area = 0

    # Iterate through all contours
    for contour in contours:
        # Calculate the area of each contour
        contour_area += cv2.contourArea(contour)

    # Display the contour area on the camera feed
    cv2.putText(frame, f"Contour Area: {contour_area}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the skin area on the camera feed
    cv2.imshow('Skin Area', frame)

    # Check for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
