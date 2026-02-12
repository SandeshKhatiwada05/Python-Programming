import cv2

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access camera")
    exit()

# Initial mode: grayscale off
grayscale = False

print("Press 'g' to toggle grayscale, 'e' for edge detection, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Apply grayscale if toggled
    display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if grayscale else frame

    # Edge detection with Canny when 'e' pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('g'):
        grayscale = not grayscale
    elif key == ord('e'):
        # If already grayscale, use it; else convert
        temp = display_frame if grayscale else cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display_frame = cv2.Canny(temp, 100, 200)
    elif key == ord('q'):
        break

    cv2.imshow("Video Filter", display_frame)

cap.release()
cv2.destroyAllWindows()
