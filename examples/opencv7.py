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

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform Canny edge detection
    edges = cv2.Canny(gray, 100, 200)  # Adjust threshold values as needed

    # Display the edge-detected frame
    cv2.imshow('Edge Detection', edges)

    # Check for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
