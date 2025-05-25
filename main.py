from sort import Sort
import os
import cv2
import csv
import numpy as np
from collections import defaultdict
from ultralytics import YOLO
from rapor_olustur import PDFReport

class VehicleDetector:
    def __init__(self, model_path, video_path, output_csv="output.csv"):
        self.model_path = model_path
        self.video_path = video_path
        self.output_csv = output_csv

        self._check_files()

        self.model = YOLO(self.model_path)
        self.class_names = self.model.names
        self.class_counts = defaultdict(int)

        self.tracker = Sort()
        self.tracked_ids = set()

        with open(self.output_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Frame", "Class", "Count", "Track_ID"])

    def _check_files(self):
        print("📁 Aktif dizin:", os.getcwd())
        if not os.path.exists(self.model_path):
            print(f"❌ Model dosyası bulunamadı: {self.model_path}")
            exit()
        if not os.path.exists(self.video_path):
            print(f"❌ Video dosyası bulunamadı: {self.video_path}")
            exit()

    def detect(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("❌ Video açılamadı.")
            return

        frame_number = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                print("✅ Video bitti.")
                break

            frame_number += 1
            results = self.model(frame)
            result = results[0]

            annotated_frame = frame.copy()
            detections = []

            for box in result.boxes:
                class_id = int(box.cls[0])
                label = self.class_names[class_id]
                if label != "car":
                    continue
                x1, y1, x2, y2 = map(float, box.xyxy[0])
                conf = float(box.conf[0])
                detections.append([x1, y1, x2, y2, conf])

            detections = np.array(detections)
            trackers = self.tracker.update(detections) if len(detections) > 0 else []

            for trk in trackers:
                x1, y1, x2, y2, track_id = map(int, trk)
                if track_id not in self.tracked_ids:
                    self.tracked_ids.add(track_id)
                    self.class_counts["car"] += 1
                    with open(self.output_csv, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([frame_number, "car", 1, track_id])

                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f"car {track_id}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            cv2.imshow("Araç Tespiti (YOLOv8 + SORT)", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("🚪 Kullanıcı çıkış yaptı.")
                break

        cap.release()
        cv2.destroyAllWindows()

        print("\n Toplam Tespitler (Tekil ID'lerle):")
        for cls, count in self.class_counts.items():
            print(f"{cls}: {count} adet")

        rapor = PDFReport(self.output_csv)
        rapor.generate()

if __name__ == "__main__":
    model_path = "yolov8n.pt"
    video_path = "trafik.mp4"
    detector = VehicleDetector(model_path, video_path)
    detector.detect()
