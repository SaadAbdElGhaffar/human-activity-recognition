import cv2
from ultralytics import YOLO
import numpy as np
import cvzone

# Load a model
model = YOLO("models/yolov8n-pose.pt") 

# Initialize video capture
cap = cv2.VideoCapture('data/input.mp4')
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Define the codec and create a VideoWriter object to save the output
output_width = 1200
output_height = 680
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output/output.mp4', fourcc, 30, (output_width, output_height))

# Define a function to calculate the angle between three keypoints
def calculate_angle(a, b, c):
    try:
        a = np.array(a)  # First point
        b = np.array(b)  # Mid point
        c = np.array(c)  # End point

        # Calculate the angle in degrees
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle
    except:
        return None

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video or failed to read frame.")
        break

    # Resize frame
    frame = cv2.resize(frame, (output_width, output_height))

    # Perform pose detection
    results = model.predict(frame, save=False)

    # Get the bounding box information in xyxy format
    boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)

    # Get the keypoints data for all detected persons
    keypoints_data = results[0].keypoints.data.cpu().numpy()
    statuses = []

    # Iterate through the detected persons
    for i, keypoints in enumerate(keypoints_data):
        # Check if keypoints are valid (COCO format: 0=nose, 11=left hip, 13=left knee)
        if len(keypoints) >= 14 and keypoints[0][2] > 0.5 and keypoints[11][2] > 0.5 and keypoints[13][2] > 0.5:
            # Calculate angle between nose (0), left hip (11), and left knee (13)
            angle = calculate_angle(keypoints[0][:2], keypoints[11][:2], keypoints[13][:2])
            if angle is not None:
                status = 'Sitting' if angle < 110 else 'Standing'
                print(f"Person {i + 1} is {status} (Angle: {angle:.2f} degrees)")
                statuses.append(status)
            else:
                statuses.append('Unknown')
        else:
            statuses.append('Unknown')

    # Draw bounding boxes and statuses on the frame, only for valid statuses
    for i, (x1, y1, x2, y2) in enumerate(boxes):
        if i < len(statuses) and statuses[i] != 'Unknown':  # Skip Unknown statuses
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cvzone.putTextRect(
                frame, f"{statuses[i]}", (x1, y2 - 10),
                scale=3, thickness=3,
                colorT=(255, 255, 255), colorR=(255, 0, 255),
                font=cv2.FONT_HERSHEY_PLAIN,
                offset=10,
                border=0, colorB=(0, 255, 0)
            )

    # Write the frame to the output video file
    out.write(frame)

    # Optionally display the frame with annotations
    cv2.imshow('YOLOv8 Pose Detection', frame)

    # Exit the program if the user presses the 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()