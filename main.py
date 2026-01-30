import cv2
import os
from ultralytics import YOLO
import detector_utils as utils

# 1. Load the AI Brain
model = YOLO("yolov8n.pt") 
cap = cv2.VideoCapture(0)

# Set resolution for better detection
cap.set(3, 1280)
cap.set(4, 720)

SAFE_DISTANCE = 200 # Adjust this if needed

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Error: Could not read from webcam.")
        break

    # 2. Run Detection
    results = model(frame, stream=True, verbose=False)
    
    centers = []
    boxes = []

    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0: # Detect only 'person'
                b = box.xyxy[0].to("cpu").numpy()
                centers.append(utils.get_center(b))
                boxes.append(b)

    # 3. Proximity Logic & Voice Alarm
    violated = set()
    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            distance = utils.calculate_distance(centers[i], centers[j])
            if distance < SAFE_DISTANCE:
                violated.add(i)
                violated.add(j)
                cv2.line(frame, centers[i], centers[j], (0, 0, 255), 3)
                
                # macOS Futuristic Voice Alarm
                # This will run in the background so the video doesn't lag
                os.system('say "Warning: Social Distance Violation" &')

    # 4. Drawing the HUD
    for i, b in enumerate(boxes):
        color = (0, 0, 255) if i in violated else (0, 255, 0)
        x1, y1, x2, y2 = map(int, b)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        
        status = "!!! WARNING !!!" if i in violated else "SAFE"
        cv2.putText(frame, status, (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # 5. Display
    cv2.imshow("AI Digital Guardian - System Active", frame)
    
    # Press 'q' to quit properly
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()