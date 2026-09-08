from ultralytics import YOLO
import cv2

# Sirf best.pt use ho raha hai
model = YOLO("best.pt") 

def detect_and_draw(frame):
    # Balanced settings: conf=0.25 (halka strict taake "No Mask" bar bar na badle) 
    # aur imgsz=640 (fast aur stable)
    results = model(frame, conf=0.25, imgsz=640, verbose=False)
    
    for result in results:
        names = model.names  # Model ke exact labels automatically le rahe hain
        boxes = result.boxes
        
        if boxes is not None and len(boxes) > 0:
            for box in boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                label = names[cls_id]
                
                # Colors (0=Improper, 1=Mask, 2=No Mask)
                if cls_id == 0:
                    color = (0, 255, 255) # Yellow
                elif cls_id == 1:
                    color = (0, 255, 0)   # Green
                else:
                    color = (0, 0, 255)   # Red
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label} {conf*100:.0f}%", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                
    return frame