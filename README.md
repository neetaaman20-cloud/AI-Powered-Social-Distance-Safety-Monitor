# 🛡️ Digital Guardian: AI-Powered Social Distance & Safety Monitor

A futuristic, real-time computer vision system that monitors human proximity and provides automated safety alerts using deep learning.

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Tech](https://img.shields.io/badge/Tech-YOLOv8%20|%20OpenCV-blue)
![Platform](https://img.shields.io/badge/Platform-macOS%20|%20Linux%20|%20Windows-lightgrey)

---

## 🚀 Overview
The **Digital Guardian** is a high-performance perception system designed for smart-city safety and workplace monitoring. It uses the **YOLOv8** (You Only Look Once) architecture to identify humans in a video stream and calculates the 3D spatial distance between them in real-time.

### **Futuristic Features**
* **Neural-Link Detection:** High-speed person detection using the YOLOv8 Nano model.
* **Real-Time Proximity Mapping:** Dynamically calculates Euclidean distance between all detected subjects.
* **Visual HUD:** A "Sci-Fi" Heads-Up Display that highlights safe zones in **Green** and violations in **Red**.
* **Automated Voice Response:** Integrated macOS `say` system that triggers audible "Warning" alerts during safety violations.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **AI Framework:** Ultralytics YOLOv8
* **Computer Vision:** OpenCV
* **Math Engine:** NumPy & SciPy (Spatial distance algorithms)

---

## 📐 The Science
The system determines safety by calculating the **Euclidean Distance** between the centroids of detected bounding boxes ($P1$ and $P2$):

$$d(P1, P2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

If the calculated distance $d$ falls below the `SAFE_DISTANCE` threshold, a violation is logged.

---

## 💻 Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Digital-Guardian.git](https://github.com/YOUR_USERNAME/Digital-Guardian.git)
   cd Digital-Guardian

   Create a Virtual Environment

Bash
python3 -m venv venv
source venv/bin/activate
Install Dependencies

Bash
pip install -r requirements.txt
Launch the Guardian

Bash
python3 main.py
