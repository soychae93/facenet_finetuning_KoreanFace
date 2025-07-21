# FaceNet - Korean Faces Fine-tuned Version

This is a fork of the original [FaceNet](https://github.com/davidsandberg/facenet) repository, fine-tuned using Korean face datasets to improve performance on Korean facial recognition tasks.

## 🔍 Motivation

The original FaceNet model was trained primarily on Western face datasets. As a result, performance on Korean faces (and more broadly, East Asian faces) may be suboptimal. This repository fine-tunes the pretrained FaceNet model on a curated dataset of Korean faces to enhance recognition accuracy in this demographic.

## 🛠️ What's Changed

- Fine-tuned the pretrained FaceNet model using a Korean face dataset.
- Updated training scripts to support additional preprocessing options (e.g., alignment method tuned for East Asian landmarks).
- Added evaluation results comparing original vs. fine-tuned model performance on Korean datasets.

## 📂 Repository Structure
facenet-korean/
│
├── src/ # Core FaceNet code (same as original)
├── fine_tuned_model/ # Checkpoints of the fine-tuned model
├── korean_dataset/ # Korean face images (not included – see below)
├── scripts/ # Training and evaluation scripts
├── README.md # You are here
└── requirements.txt

## 📊 Performance

The fine-tuned FaceNet model demonstrates excellent performance on Korean face verification tasks:

| **Metric**                     | **Value**                         |
|-------------------------------|-----------------------------------|
| **Accuracy**                  | 0.9955 ± 0.00342                  |
| **Validation Rate**           | 0.9860 ± 0.00975 @ FAR = 0.00100 |
| **Area Under Curve (AUC)**    | 1.000                             |
| **Equal Error Rate (EER)**    | 0.004                             |

These results suggest the model is highly effective for Korean facial recognition scenarios.


