# 🕵️‍♂️ AI Proctor

A modern, AI-powered online exam proctoring system with real-time face/head monitoring, object detection, and a proctor dashboard.

---

## 📋 Table of Contents

- [🚀 Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [⚙ Installation](#-installation)
- [🔧 Configuration](#-configuration)
- [📁 Project Structure](#-project-structure)
- [📚 Usage Guide](#-usage-guide)
- [🚀 Deployment](#-deployment)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
- [📞 Support](#-support)

---

## 🚀 Features

- 👤 **User Authentication** (Student login with roll number)
- 📝 **Online Exam Interface** (MCQs, timer, auto-submit)
- 🖥 **Fullscreen Enforcement** (Auto-submit on exit)
- 🎥 **Webcam Proctoring** (Face registration, live face verification)
- 🧑‍🤝‍🧑 **Multiple Face Detection** (Auto-submit if more than one face)
- 🤳 **Object Detection** (Detects phones, laptops, etc. and auto-submits)
- 🧑‍💻 **Head Movement Tracking** (Detects suspicious head movement)
- 📊 **Proctor Dashboard** (Live alerts, analytics, and charts)
- 🛡 **Anti-cheating Measures** (Logs, auto-submission, and alerts)

---

## 🛠 Tech Stack

- **Frontend:** React, Bootstrap, React Webcam, Recharts
- **Backend:** Flask, Flask-CORS, OpenCV, MediaPipe, YOLOv5 (PyTorch)
- **AI/ML:** MediaPipe (face detection), YOLOv5 (object detection)
- **Other:** Python, JavaScript, HTML/CSS

---

## ⚙ Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/ai-proctor.git
   cd ai-proctor
   ```

2. **Frontend Setup:**
   ```sh
   cd ai-proctor
   npm install
   ```

3. **Backend Setup:**
   ```sh
   cd backend
   python -m venv venv
   venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux

   pip install -r requirements.txt
   # Or manually:
   pip install flask flask-cors opencv-python mediapipe torch torchvision yolov5
   ```

---

## 🔧 Configuration

- **Frontend:**  
  - Update API URLs in React if your backend runs on a different port.
- **Backend:**  
  - Ensure YOLOv5 model weights are downloaded on first run.
  - Set CORS as needed for your deployment.

---

## 📁 Project Structure

```
ai-proctor/
  ├── ai-proctor/           # React frontend
  │   ├── src/
  │   │   ├── components/
  │   │   ├── pages/
  │   │   ├── App.js
  │   │   └── App.css
  │   └── public/
  ├── backend/              # Flask backend
  │   ├── venv/
  │   └── app.py
  ├── requirements.txt
  └── README.md
```

---

## 📚 Usage Guide

1. **Start the backend:**
   ```sh
   cd backend
   venv/Scripts/activate  # or source venv/bin/activate
   python app.py
   ```

2. **Start the frontend:**
   ```sh
   cd ai-proctor
   npm start
   ```

3. **Workflow:**
   - Student logs in with roll number.
   - Reads instructions and acknowledges.
   - Registers face before exam starts.
   - Exam runs in fullscreen; webcam monitors face, head, and objects.
   - Alerts and logs are sent to the proctor dashboard.
   - Proctor can view live analytics and logs.

---

## 🚀 Deployment

- **Frontend:** Deploy with Vercel, Netlify, or any static hosting.
- **Backend:** Deploy Flask app on Heroku, AWS, or any Python server.
- **Environment Variables:** Set backend API URLs as needed for production.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/)
- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5)
- [React](https://reactjs.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Recharts](https://recharts.org/)
- Open source contributors and the AI/ML community

---

## 📞 Support

For questions, issues, or feature requests, please open an issue on [GitHub](https://github.com/yourusername/ai-proctor/issues) or contact [your.email@example.com](kartikbansal9152@gmail.com). 
