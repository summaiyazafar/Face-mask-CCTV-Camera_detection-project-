from ultralytics import YOLO

def main():
    model = YOLO("yolo11n.pt")

    results = model.train(
        data="data.yaml",
        epochs=50,
        imgsz=416,
        batch=8,
        device="cpu",
        patience=20,
        project="mask_detection",
        name="yolov11_mask_v1",
        val=True,
    )

    print("Training complete!")
    print("Best weights saved at: mask_detection/yolov11_mask_v1/weights/best.pt")

    metrics = model.val(data="data.yaml", split="test")
    print(metrics)


if __name__ == "__main__":
    main()