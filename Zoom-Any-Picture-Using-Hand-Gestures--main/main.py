import cv2
from cvzone.HandTrackingModule import HandDetector
import os

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the hand detector
detector = HandDetector(detectionCon=0.7)
startDis = None
scale = 0
cx, cy = 200, 200
moveX, moveY = 0, 0
moveMode = False

# Load all images in the directory
image_folder = "images"  # Folder containing the images
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
current_image_index = 0
img1 = cv2.imread(image_files[current_image_index])

# Create the main display window
cv2.namedWindow("Problem Solve with Ridoy")

# Slider window
cv2.namedWindow("Controls", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Controls", 400, 70)  # Resize the window to better fit the slider

# Function to update scale based on slider
def update_scale(x):
    global scale
    scale = x - 100  # Center the scale around 0

cv2.createTrackbar("Zoom", "Controls", 100, 200, update_scale)

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global scale
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            scale += 10
        else:
            scale -= 10

cv2.setMouseCallback("Problem Solve with Ridoy", mouse_callback)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if len(hands) == 2:
        hand1 = hands[0]
        hand2 = hands[1]

        hand1_fingers = detector.fingersUp(hand1)
        hand2_fingers = detector.fingersUp(hand2)

        if hand1_fingers == [1, 1, 0, 0, 0] and hand2_fingers == [1, 1, 0, 0, 0]:
            if startDis is None:
                length, info, img = detector.findDistance(hand1["center"], hand2["center"], img)
                startDis = length

            length, info, img = detector.findDistance(hand1["center"], hand2["center"], img)
            scale = int((length - startDis) // 2)
            cx, cy = info[4:]

    elif len(hands) == 1:
        hand = hands[0]
        hand_fingers = detector.fingersUp(hand)

        if hand_fingers == [0, 1, 0, 0, 0]:  # Index finger up
            if not moveMode:
                moveX, moveY = hand["center"]
                moveMode = True
            else:
                cx += hand["center"][0] - moveX
                cy += hand["center"][1] - moveY
                moveX, moveY = hand["center"]
        else:
            moveMode = False

    else:
        startDis = None
        moveMode = False

    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('+'):
        scale += 10
    elif key == ord('-'):
        scale -= 10
    elif key == ord('n'):  # Next image
        current_image_index = (current_image_index + 1) % len(image_files)
        img1 = cv2.imread(image_files[current_image_index])
        scale = 0  # Reset scale for the new image
    elif key == ord('p'):  # Previous image
        current_image_index = (current_image_index - 1) % len(image_files)
        img1 = cv2.imread(image_files[current_image_index])
        scale = 0  # Reset scale for the new image

    try:
        h1, w1, _ = img1.shape
        newH, newW = h1 + scale, w1 + scale
        if newH > 0 and newW > 0:
            img1_resized = cv2.resize(img1, (newW, newH))

        # Ensure the image is within bounds
        cx = min(max(cx, newW // 2), img.shape[1] - newW // 2)
        cy = min(max(cy, newH // 2), img.shape[0] - newH // 2)

        # Ensure the image is drawn within the window bounds
        top_left_x = max(cx - newW // 2, 0)
        top_left_y = max(cy - newH // 2, 0)
        bottom_right_x = min(cx + newW // 2, img.shape[1])
        bottom_right_y = min(cy + newH // 2, img.shape[0])

        img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = img1_resized[:bottom_right_y - top_left_y, :bottom_right_x - top_left_x]
    except Exception as e:
        print(f"Error: {e}")
        pass

    cv2.imshow("Problem Solve with Ridoy", img)

cap.release()
cv2.destroyAllWindows()
