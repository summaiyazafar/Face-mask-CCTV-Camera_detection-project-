# 😷 Face Mask Detection System (CCTV, webcam, youtube videos / YOLOv11)

**Real-time AI-powered face mask compliance monitoring** — webcam, IP/CCTV cameras, YouTube videos, ya saved video files, kisi bhi source se kaam karta hai.

Model teen classes detect karta hai:
- ✅ **Mask** — properly worn
- ⚠️ **Improper Mask** — galat tareeqe se pehna hua (naak khuli, thodi neeche)
- ❌ **No Mask** — mask nahi pehna

---

## 📌 Yeh System Kyun Zaroori Hai

Public health guidelines follow karwana manually mushkil hota hai — har jagah ek insaan khada nahi ho sakta jo 24/7 dekhta rahe ke log mask pehne hain ya nahi. Yeh system **automatically, real-time**, aur **bina kisi manual effort ke** compliance monitor karta hai, aur jahan chahein wahan record bhi generate kar sakta hai.

---

## 🏥 Real-World Use Cases

Yeh system kisi bhi jagah deploy ho sakta hai jahan health/safety compliance zaroori ho:

### 🏥 Hospitals & Clinics
- Reception, waiting areas, aur wards ki entry points par mask compliance monitor karna
- Immunocompromised patients ke wards mein extra strict monitoring
- Infection control teams ke liye automatic compliance reports

### 🍳 Hotels, Restaurants & Commercial Kitchens
- Kitchen staff ki hygiene compliance (mask + food safety regulations)
- Food handling areas mein continuous monitoring, jahan human supervisor har waqt maujood nahi ho sakta
- Health inspection audits ke liye recorded proof

### 🏭 Factories & Industrial Units
- Production floors jahan dust masks ya safety masks mandatory hon
- Pharma aur chemical manufacturing units jahan contamination control critical hai

### 🏫 Schools, Colleges & Universities
- Classrooms, corridors, aur cafeterias mein entry-level compliance check
- Outbreak ke dauran real-time monitoring bina extra staff hire kiye

### 🛍️ Malls, Retail Stores & Supermarkets
- Entry gates par automatic screening
- High-footfall areas mein crowd health-safety monitoring

### 🚉 Public Transport (Airports, Bus/Train Stations)
- High-density areas jahan disease transmission risk zyada hota hai
- Terminal entries aur waiting lounges mein monitoring

### 🏢 Corporate Offices
- Reception aur meeting rooms mein compliance
- Return-to-office policies ko enforce karne ke liye

### 🕌 Mosques, Churches & Public Gathering Places
- Bade gatherings ke dauran health protocols maintain karwane ke liye

---

## 💡 Business Value

| Fayda | Kaise |
|---|---|
| **Manpower ki bachat** | Ek dedicated insaan ki zaroorat nahi, camera khud monitor karta hai |
| **24/7 Monitoring** | Insaan thak sakta hai, system nahi rukta |
| **Instant Records** | Detection wali video automatically save hoti hai — audit/compliance proof ke liye |
| **Scalable** | Ek CCTV network mein multiple cameras par ek saath laga sakte hain |
| **Cost-Effective** | Sirf ek trained model + existing cameras — naya hardware lagbhag zaroori nahi |
| **Flexible Deployment** | Laptop webcam se le kar enterprise-level CCTV tak, sab pe kaam karta hai |

---

## 🎥 Supported Detection Sources

| Source | Use Case |
|---|---|
| 💻 **Laptop/Webcam** | Quick testing, chhoti setups, reception desks |
| 📹 **CCTV / IP Camera (RTSP)** | Real deployment — hospitals, factories, offices |
| ▶️ **YouTube Video** | Demo/testing bina apni camera lagaye |
| 📁 **Local Video Folder** | Bulk testing — pehle se recorded footage par model accuracy check karna |

---

## 📂 Project Structure

```
Face Mask CCTV.v1-cctv_mask_detection_v1.yolov11/
├── main.py              # Entry point
├── camera.py             # Video source handling (webcam / IP / folder)
├── detector.py            # YOLO model + bounding boxes draw karna
├── config.py               # Saari settings yahan se control hoti hain
├── check_ip.py              # IP camera connection test
├── train_more.py             # Existing model ko aur train karna
├── best.pt                    # Trained YOLO weights
├── models/                     # Different training versions
├── videos/                      # Test videos (folder mode)
└── runs/
    └── detect/
        ├── train.../           # Training results
        └── predict.../          # Detection output videos
```

---

## ⚙️ Installation

```bash
pip install ultralytics opencv-python
```

YouTube detection ke liye (optional):
```bash
pip install -U yt-dlp yt-dlp-ejs
winget install DenoLand.Deno
```
*(Deno install karne ke baad terminal restart karein.)*

---

## 🚀 Kaise Use Karein

Sab kuch `config.py` ke `CAMERA_MODE` se control hota hai:

```python
CAMERA_MODE = "laptop"   # "laptop" | "ip" | "youtube" | "folder"
```

### 1️⃣ Webcam Detection
```python
CAMERA_MODE = "laptop"
```
```bash
python main.py
```

### 2️⃣ CCTV / IP Camera Detection
```python
CAMERA_MODE = "ip"
IP_ADDRESS = "192.168.1.47"
RTSP_USERNAME = "admin"
RTSP_PASSWORD = "123456"
RTSP_PORT = "554"
RTSP_PATH = "/unicast/c1/s0/live"
```
```bash
python check_ip.py   # pehle connection test karein
python main.py
```

### 3️⃣ YouTube Video Detection
```python
CAMERA_MODE = "youtube"
YOUTUBE_URL = "https://www.youtube.com/watch?v=XXXXXXXXX"
```
```bash
python main.py
```

### 4️⃣ Local Video Folder (Batch Testing)
```python
CAMERA_MODE = "folder"
VIDEO_FOLDER = "videos"
```
```bash
python main.py
```
**Controls:** `n` = agli video | `q` = program band karo

Detection wali videos automatically save hoti hain:
```
runs/detect/predict/<video_naam>_detected.mp4
```

---

## 🧠 Model Training / Fine-tuning

Existing `best.pt` ko aur epochs ke saath improve karne ke liye:

```python
from ultralytics import YOLO

model = YOLO("best.pt")
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    device=0,          # GPU: 0 | CPU: "cpu"
    project="runs/detect",
    name="train_extended",
)
```

Naya model: `runs/detect/train_extended/weights/best.pt`

---

## 🎨 Detection Color Legend

| Class | Color |
|---|---|
| 🟢 Mask | Green |
| 🔴 No Mask | Red |
| 🟡 Improper Mask | Yellow |

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| `cv2`/`ultralytics` import error | VS Code mein sahi Python interpreter select karein |
| IP camera connect nahi ho rahi | `check_ip.py` se test karein, RTSP path/credentials verify karein |
| YouTube video fail ho rahi | Deno + `yt-dlp` update karein, VPN/antivirus SSL scan off karein |
| Detection slow/laggy | `imgsz` chhota karein ya GPU use karein |

---

## 🌍 Future Scope

- Real-time SMS/Email alerts jab "No Mask" detect ho
- Multi-camera dashboard (ek saath saari branches/floors monitor karna)
- Cloud-based compliance reporting aur analytics
- Mobile app integration for live alerts

---

## 📄 License

Yeh project educational aur commercial deployment dono ke liye customize kiya ja sakta hai.
