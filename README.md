# Human Activity Recognition using Pose Estimation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8.svg)](https://opencv.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF.svg)](https://github.com/ultralytics/ultralytics)
[![NumPy](https://img.shields.io/badge/NumPy-1.21+-013243.svg)](https://numpy.org/)
[![CVZone](https://img.shields.io/badge/CVZone-1.5+-FF6B35.svg)](https://github.com/cvzone/cvzone)

A Python application that uses YOLOv8 pose estimation to detect and classify human activities (sitting/standing) in videos in real-time.

## Demo

![Demo](output/output.gif)

*The application detects human poses and classifies activities as "Sitting" or "Standing" based on body angle analysis.*

## Features

- Real-time human pose detection using YOLOv8
- Activity classification (Sitting/Standing) based on body angles
- Video processing with bounding box annotations
- Output video generation with activity labels

## Project Structure

```
human-activity-recognition/
├── activity_recognizer.py      # Main application script
├── data/                       # Input / sample videos (keep small examples only)
│   └── input.mp4               # Sample input video
├── models/                     # Pre-trained / fine-tuned models
│   └── yolov8n-pose.pt         # YOLOv8 pose estimation model
├── output/                     # Generated outputs (videos, gifs) - usually gitignored except demo
│   ├── output.mp4              # Example processed video (may be regenerated)
│   └── output.gif              # Demo GIF shown in README
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT license
└── README.md                   # Project docs
```

## Requirements

- Python 3.7+
- OpenCV (cv2)
- Ultralytics YOLO
- NumPy
- cvzone

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Human-activities-recognition-using-pose-estimation--main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python activity_recognizer.py
   ```

## How it Works

1. **Pose Detection**: Uses YOLOv8 to detect human keypoints in each frame
2. **Angle Calculation**: Calculates angles between nose, hip, and knee joints
3. **Activity Classification**: Classifies as "Sitting" if angle < 110°, "Standing" otherwise
4. **Visualization**: Draws bounding boxes and activity labels on the output video

## Output

The application generates:
- `output/output.mp4`: Processed video with pose detection and activity classification
- Real-time display window showing the detection results

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact
- **GitHub:** [SaadAbdElGhaffar](https://github.com/SaadAbdElGhaffar)  
- **LinkedIn:** [Saad Abd El-Ghaffar](https://www.linkedin.com/in/saadabdelghaffar/)  
- **Email:** [saad.abdelghaffar.ai@gmail.com](mailto:saad.abdelghaffar.ai@gmail.com)  
- **Kaggle:** [@abdocan](https://www.kaggle.com/abdocan)

---

⭐ **Star this repository if you found it helpful!**
