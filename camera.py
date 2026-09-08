import cv2
import config

def open_camera():
    if config.CAMERA_MODE == "laptop":
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Failed to open laptop webcam")
            return None
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        print("Laptop webcam connected successfully.")
        return cap

    elif config.CAMERA_MODE == "ip":  # <--- Yahan "ip" likha hai, "laptop" nahi!
        url = f"rtsp://{config.RTSP_USERNAME}:{config.RTSP_PASSWORD}@{config.IP_ADDRESS}:{config.RTSP_PORT}{config.RTSP_PATH}"
        print(f"Trying to connect: {url}")
        cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        cap.set(cv2.CAP_PROP_FPS, 20)

        if not cap.isOpened():
            print("Failed to open IP Camera. (Check IP/Password in config.py)")
            return None
        print("IP Camera connected successfully.")
        return cap

    else:
        print("Invalid CAMERA_MODE")
        return None

def read_frame(cap):
    # Frame skip nahi karte, taake har koi detect ho
    ret, frame = cap.read()
    return ret, frame

def close_camera(cap):
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()