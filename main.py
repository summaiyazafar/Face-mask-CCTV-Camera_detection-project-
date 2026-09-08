import cv2
from camera import open_camera, read_frame, close_camera
from detector import detect_and_draw

def main():
    cap = open_camera()
    if cap is None:
        print("Exiting...")
        return

    print("Mask Detection Started. Press 'q' to quit.")
    
    while True:
        ret, frame = read_frame(cap)
        if not ret:
            print("Failed to grab frame")
            break

        frame = detect_and_draw(frame)
        cv2.imshow("Mask Detection CCTV", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    close_camera(cap)

if __name__ == "__main__":
    main()