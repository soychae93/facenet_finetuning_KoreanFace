# FaceNet - Korean Faces Fine-tuned Version

This is a fork of the original [FaceNet](https://github.com/davidsandberg/facenet) repository, fine-tuned using Korean face datasets to improve performance on Korean facial recognition tasks.

## 🔍 Motivation

The original FaceNet model was trained primarily on Western face datasets. As a result, performance on Korean faces (and more broadly, East Asian faces) is suboptimal. This repository fine-tunes the pretrained FaceNet model on a curated dataset of Korean faces to enhance recognition accuracy in this demographic.

## 🛠️ What's Changed

- Fine-tuned the pretrained FaceNet model using a Korean face dataset.
- Updated training scripts to support additional preprocessing options (e.g., alignment method tuned for East Asian landmarks).
- Evaluated fine-tuned model performance on Korean datasets.

## 🔁 Evaluation with New Data

### 🧩 1. Align Your Dataset Using MTCNN

This step crops the faces from new images using MTCNN:
```bash
#!/bin/bash

export PYTHONPATH=/home/schae/lsmm_proj/facenet-master/src
for N in {1..4}; do \
python /user/facenet-master/src/align/align_dataset_mtcnn.py \
/user/facenet-master/datasets/lfw/K-face_mtcnn/ \
/user/facenet-master/datasets/K-face_160 \
--image_size 160 \
--margin 32 \
--random_order \
--gpu_memory_fraction 0.25 \
& done

To evaluate the fine-tuned model on a new dataset, use the following command:

#!/bin/bash

python3 src/validate_on_newfaces.py \
    /home/user \
    /home/facenet-master/finetuned_models/20200517-21222 \
    --distance_metric 1 \
    --use_flipped_images \
    --subtract_mean \
    --use_fixed_image_standardization \
    --lfw_pairs /home/jspark/Downloads/pairs_user.txt \
    --lfw_batch_size 78 \
    --lfw_nrof_folds 2

To load results, use the following command:
#!/bin/bash
python3 load_result.py\

*Please update the directory paths (/user/...) according to your environment.

## 📊 Performance
The fine-tuned FaceNet model demonstrates excellent performance on Korean face:

verification tasks:
## 📊 Evaluation Results: Pre-trained vs. Fine-tuned Model
- **Subgroup**: Evaluation metrics computed on **specific subsets of images**, such as those containing variations in **accessories** (e.g., sunglasses, glasses), **clothing**, or **viewpoint angle**. 
- **Total**: Evaluation metrics computed on the **entire dataset**, representing the model's **overall face recognition performance** without separating by condition.

The improvement in both subgroup and total metrics after fine-tuning indicates that the model not only performs well in general, but also maintains high accuracy across challenging face conditions (e.g., occlusion or appearance changes).


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
ㅗ

These results suggest the model is highly effective for Korean facial recognition scenarios.

