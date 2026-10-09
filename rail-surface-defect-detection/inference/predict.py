
from pathlib import Path
from ultralytics import YOLO
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Detect railway rail-surface defects."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Path to an image, video, or folder."
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Confidence threshold."
    )
    args = parser.parse_args()

    project_dir = Path(__file__).resolve().parents[1]
    weights = project_dir / "weights" / "best.pt"

    model = YOLO(str(weights))
    model.predict(
        source=args.source,
        imgsz=640,
        conf=args.conf,
        save=True
    )

if __name__ == "__main__":
    main()