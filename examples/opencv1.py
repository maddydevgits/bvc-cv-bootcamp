import cv2

# Load an image
image = cv2.imread('test.jpeg')

# Check if the image was loaded successfully
if image is not None:
    # Display the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)  # Wait for any key to be pressed
    cv2.destroyAllWindows()  # Close all OpenCV windows
else:
    print("Failed to load the image.")