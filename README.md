# FaceNet - Korean Faces Fine-tuned Version

This is a fork of the original [FaceNet](https://github.com/davidsandberg/facenet) repository, fine-tuned using Korean face datasets to improve performance on Korean facial recognition tasks.

## 🔍 Motivation

The original FaceNet model was trained primarily on Western face datasets. As a result, performance on Korean faces (and more broadly, East Asian faces) is suboptimal. This repository fine-tunes the pretrained FaceNet model on a curated dataset of Korean faces to enhance recognition accuracy in this demographic.

## 🛠️ What's Changed

- Fine-tuned the pretrained FaceNet model using a Korean face dataset.
- Updated training scripts to support additional preprocessing options (e.g., alignment method tuned for East Asian landmarks).
- Evaluated fine-tuned model performance on Korean datasets.

---

## 🏆 Results

> 📈 **Fine-tuning with Korean facial data significantly improved model performance**, especially for faces with occlusions (e.g., glasses, sunglasses) or varied viewpoints.
>
> ✅ **Overall accuracy improved from 74.6% to 93.0%**  
> ✅ **Subgroup accuracy (e.g., glasses/clothing/angles) improved from 78.3% to 95.6%**  
> ✅ **False acceptance rate (FAR) decreased by over 75%**

### 📊 Evaluation Results: Pre-trained vs. Fine-tuned Model

| **Category** | **Metric**    | **Pre-trained**            | **Fine-tuned**            |
|--------------|---------------|----------------------------|---------------------------|
| **Subgroup** | Threshold     | 0.37                       | 0.4                       |
|              | Accuracy      | 0.783                      | 0.956                     |
|              | VAL           | 0.923                      | 0.983                     |
|              | FAR           | 0.356                      | 0.072                     |
|              | AUC           | 0.910                      | 0.994                     |
| **Total**    | Threshold     | 0.37                       | 0.4                       |
|              | Accuracy      | 0.746                      | 0.930                     |
|              | VAL           | 0.774                      | 0.933                     |
|              | FAR           | 0.283                      | 0.073                     |
|              | AUC           | 0.830                      | 0.983                     |

### 📝 Notes on Categories

- **Subgroup**: Evaluation metrics computed on **specific subsets of images**, such as those containing variations in **accessories** (e.g., sunglasses, glasses), **clothing**, or **viewpoint angle**.  
- **Total**: Evaluation metrics computed on the **entire dataset**, representing the model's overall recognition performance.

---

## 🔁 Evaluation with New Data
...
