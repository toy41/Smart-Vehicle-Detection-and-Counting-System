# Vehicle Detection and Counting with YOLOv8 and SORT

A Python-based application that detects and counts vehicles in a video using the YOLOv8 object detection model and SORT tracking algorithm.

##  Features

- Vehicle detection using YOLOv8
- Object tracking with SORT algorithm
- Unique vehicle counting (based on tracking IDs)
- Real-time display of detections on video frames
- CSV logging of detections
- PDF report generation

## Installation

### Prerequisites

- Python 3.8+
- YOLOv8
- OpenCV
- Ultralytics
- reportlab

### Steps

1. Clone the repository:

```bash
git clone https://github.com/yourusername/vehicle-detection.git
cd vehicle-detection
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your model and video file:
   - `yolov8n.pt` (YOLOv8 model)
   - `trafik.mp4` (video file)

##  Usage

Run the application:

```bash
python main.py
```

- Press `q` to stop the camera feed manually.
- Results will be saved to `output.csv` and `report.pdf`.

## Technology Stack

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- SORT Tracking
- ReportLab (PDF)

## Output Files

- `output.csv`: Logs detected vehicle classes, frame number, and tracking IDs
- `report.pdf`: A summary PDF report generated from the CSV file

---

<a href="https://github.com/cihangirknt" target="_blank">
  <img src="https://avatars.githubusercontent.com/cihangirknt?v=4" width="50px" alt="cihangirknt"/>
  cihangirknt
</a>

<a href="https://github.com/mertaltundal" target="_blank">
  <img src="https://avatars.githubusercontent.com/mertaltundal?v=4" width="50px" alt="mertaltundal"/>
  mertaltundal
</a>

<a href="https://github.com/mertaltundal" target="_blank">
  <img src="https://avatars.githubusercontent.com/VALDEARD?v=4" width="50px" alt="VALDEARD"/>
  VALDEARD
</a>



