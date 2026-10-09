# Railway Track Monitoring Using YOLOv8

This repository provides two trained YOLOv8 models for computer-vision-based railway track inspection: a rail-surface defect detection model and a sleeper-defect instance segmentation model. The models are intended to support research into automated, image-based railway infrastructure monitoring.

The repository includes trained weights, inference scripts, training configurations, selected training results, and instructions for running inference.

## 1. Project Overview

Railway infrastructure inspection requires the identification of defects that may affect track condition and operational safety. Computer vision offers a potential approach to automating parts of this process using images acquired during inspection.

This project provides two complementary models:

| Model                         | Architecture | Task                  | Input image size |
| ----------------------------- | ------------ | --------------------- | ---------------- |
| Rail-surface defect detection | YOLOv8n      | Object detection      | 640              |
| Sleeper-defect segmentation   | YOLOv8s-seg  | Instance segmentation | 1024             |

The models address different visual inspection tasks and are provided as separate, independently executable inference pipelines.

## 2. Repository Structure

```text
railway-track-monitoring-yolov8/
├── rail-surface-defect-detection/
│   ├── weights/
│   │   └── best.pt
│   ├── inference/
│   │   └── predict.py
│   ├── training/
│   │   ├── args.yaml
│   │   └── results.csv
│   ├── results/
│   └── examples/
├── sleeper-defect-segmentation/
│   ├── weights/
│   │   └── best.pt
│   ├── inference/
│   │   └── predict.py
│   ├── training/
│   │   ├── args.yaml
│   │   └── results.csv
│   ├── results/
│   └── examples/
├── requirements.txt
└── README.md
```

The `weights` directories contain the trained model checkpoints. The `inference` directories contain the scripts used to run predictions. Training configurations and selected results are provided for reference and transparency.

## 3. Model Descriptions

### 3.1 Rail-Surface Defect Detection

This model uses **YOLOv8n**, an Ultralytics YOLO object-detection architecture, to identify and localize visual categories associated with railway rail surfaces.

The model has five classes:

1. `Cracks`
2. `Rails`
3. `Scars`
4. `breaks`
5. `lightbands`

The class names are preserved from the dataset configuration. Their exact interpretation should follow the annotation definitions provided with the source dataset.

**Model weights:** `rail-surface-defect-detection/weights/best.pt`

**Inference resolution:** 640 pixels, as configured in the inference script.

### 3.2 Sleeper-Defect Instance Segmentation

This model uses **YOLOv8s-seg** to identify and segment annotated railway sleeper-related objects and defect categories at the instance level.

The model has three classes:

1. `Crack`
2. `Popout`
3. `Sleeper`

The `Sleeper` class is included in the original dataset configuration and should not automatically be interpreted as a defect class. The classes represent the categories defined in the source annotations.

**Model weights:** `sleeper-defect-segmentation/weights/best.pt`

**Inference resolution:** 1024 pixels, as configured in the inference script.

## 4. Installation

### Requirements

* Python
* Ultralytics YOLO
* Dependencies specified in `requirements.txt`

A Windows environment is used in the example commands below. Equivalent commands can be adapted for Linux or macOS.

Clone the repository:

```bash
git clone <https://github.com/RezaFirouz3007/railway-track-monitoring-yolov8>
cd railway-track-monitoring-yolov8
```

Replace `<https://github.com/RezaFirouz3007/railway-track-monitoring-yolov8>` with the HTTPS URL of this GitHub repository.

Create and activate a virtual environment (recommended):

```bash
py -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```bash
py -m pip install -r requirements.txt
```

If the `py` launcher is unavailable, use the appropriate Python executable for your system.

## 5. Running Inference

Both models can process an image, video, or directory supported by Ultralytics YOLO.

Run the commands from the repository root.

### 5.1 Rail-Surface Defect Detection

```bash
py rail-surface-defect-detection/inference/predict.py --source "path/to/image.jpg"
```

To change the confidence threshold:

```bash
py rail-surface-defect-detection/inference/predict.py --source "path/to/image.jpg" --conf 0.25
```

The default confidence threshold is `0.25`, and the inference image size is 640.

### 5.2 Sleeper-Defect Instance Segmentation

```bash
py sleeper-defect-segmentation/inference/predict.py --source "path/to/image.jpg"
```

To change the confidence threshold:

```bash
py sleeper-defect-segmentation/inference/predict.py --source "path/to/image.jpg" --conf 0.25
```

The default confidence threshold is `0.25`, and the inference image size is 1024.

### Output

The scripts use the Ultralytics prediction interface and save visualized prediction results in the default output directories, typically:

* Detection: `runs/detect/predict/`
* Segmentation: `runs/segment/predict/`

Ultralytics may create numbered directories for subsequent runs. Output locations can vary with the installed version and settings.

## 6. Training Information and Evaluation

Selected training configurations, CSV logs, and plots are included in the corresponding model directories where available.

These materials provide information about the training process and can support further investigation of model performance.

**No numerical performance metrics are reported in this README at present.** Metrics should be added only after confirming the checkpoint to which they correspond, the evaluation dataset split, and the calculation method. In particular, training or validation results should not be presented as independent test-set performance.

For a rigorous research evaluation, report the following where available:

* Precision and recall
* Mean average precision at IoU 0.50 (mAP@0.50)
* Mean average precision across IoU thresholds 0.50–0.95 (mAP@0.50:0.95)
* For instance segmentation, mask-based metrics in addition to bounding-box metrics
* The evaluation split, sample count, and relevant evaluation settings

The included training logs are not, by themselves, evidence of performance on an independent test set.

## 7. Datasets and Attribution

The models were trained using datasets obtained from Roboflow Universe. The corresponding dataset configurations identify both source datasets as licensed under **CC BY 4.0**.

### Rail-Surface Defect Dataset

* Source: [Rail Surface Defects — Roboflow Universe](https://universe.roboflow.com/dataset-aq7x0/rail-surface-defects-flrty/dataset/3)
* Dataset version: 3
* License stated in the dataset configuration: CC BY 4.0

### Sleeper-Defect Dataset

* Source: [Sleepers Defects — Roboflow Universe](https://universe.roboflow.com/mercury-zypvz/sleepers-defects/dataset/10)
* Dataset version: 10
* License stated in the dataset configuration: CC BY 4.0

Please consult the original dataset pages for the dataset descriptions, annotation definitions, attribution requirements, and current licensing terms.

The dataset licenses do not automatically establish the licensing status of the trained model weights, inference code, or other repository materials. Users should verify the relevant rights and obligations before redistributing or commercially using these materials.

## 8. Limitations

These models are research tools and should not be treated as validated railway safety systems.

* **Dataset dependence:** Results may depend on the source datasets, annotation conventions, and diversity of the training images.
* **Generalization:** Performance on different railway networks, rail materials, sleeper types, lighting conditions, weather conditions, camera systems, or image resolutions has not been established by the information provided here.
* **Detection versus segmentation:** The rail-surface model predicts object locations, while the sleeper model produces instance masks. Their outputs and evaluation metrics are not directly interchangeable.
* **False predictions:** Both models may produce false positives or miss defects. Predictions require appropriate validation before being used for operational decisions.
* **Operational validation:** Independent testing and domain-specific validation are required before considering deployment in railway inspection workflows.

These models are intended to support research and experimentation rather than replace qualified inspection procedures.

## 9. Software, Model Weights, and Licensing

The repository contains software and trained model weights. Their licensing status must be considered separately from the licenses of the source datasets.

The source dataset configurations identify CC BY 4.0. This does not, by itself, mean that the code, trained weights, or the entire repository can be redistributed under CC BY 4.0.

Before assigning a repository-wide license or distributing the weights, confirm the applicable terms for:

* The original datasets and their annotations
* The trained model weights and any relevant restrictions on derived models
* Ultralytics YOLO and its applicable licensing terms
* Third-party code or other materials included in the repository

Until those checks are complete, do not assume that every repository component is cleared for unrestricted reuse. Any license added to the repository should accurately reflect the rights held by the author and the obligations associated with its contents.

## 10. Citation

If you use these models in a research article, report, thesis, or other scholarly work, cite the repository and identify the model used.

A suggested provisional reference is:

> Mohammadi-Firouz, R. *Railway Track Monitoring Using YOLOv8: Rail-Surface Defect Detection and Sleeper-Defect Instance Segmentation*. GitHub repository.

Replace this provisional reference with the verified author name, publication or release year, repository URL, version, and DOI if available. A DOI should be included only after an archival release has been created and a DOI has actually been assigned.

For reproducibility, also report the model architecture, checkpoint, software environment, dataset version, evaluation split, and inference settings relevant to your results.

## 11. Acknowledgements

The source datasets are hosted on Roboflow Universe. Please refer to the linked dataset pages for source information and required attribution.

The models use the Ultralytics YOLO framework. Refer to the [Ultralytics documentation](https://docs.ultralytics.com/) for framework information and the applicable licensing terms.

---

**Repository purpose:** Research and development of computer-vision methods for railway track monitoring.

For questions about the models, their configuration, or their use in research, please open an issue in this repository.
