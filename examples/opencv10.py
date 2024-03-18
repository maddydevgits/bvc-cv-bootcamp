import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera, you can change it if you have multiple cameras

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec used to write the video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Output file name, codec, fps, frame size

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    # Write the frame into the video file
    out.write(frame)

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Check for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects and close the OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()
