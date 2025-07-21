# FaceNet - Korean Faces Fine-tuned Version

This is a fork of the original [FaceNet](https://github.com/davidsandberg/facenet) repository, fine-tuned using Korean face datasets to improve performance on Korean facial recognition tasks.

## 🔍 Motivation

The original FaceNet model was trained primarily on Western face datasets. As a result, performance on Korean faces (and more broadly, East Asian faces) is suboptimal. This repository fine-tunes the pretrained FaceNet model on a curated dataset of Korean faces to enhance recognition accuracy in this demographic.

## 🛠️ What's Changed

- Fine-tuned the pretrained FaceNet model using a Korean face dataset.
- Updated training scripts to support additional preprocessing options (e.g., alignment method tuned for East Asian landmarks).
- Evaluated fine-tuned model performance on Korean datasets.

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

## 🔁 Evaluation with New Data

Once you have aligned and prepared your own dataset, you can evaluate the fine-tuned model as follows.

### 🧩 1. Align Your Dataset Using MTCNN

This step crops the faces from new images using MTCNN:

```bash
#!/bin/bash

export PYTHONPATH=/home/schae/lsmm_proj/facenet-master/src

for N in {1..4}; do
    python /user/facenet-master/src/align/align_dataset_mtcnn.py \
        /user/facenet-master/datasets/lfw/K-face_mtcnn/ \
        /user/facenet-master/datasets/K-face_160 \
        --image_size 160 \
        --margin 32 \
        --random_order \
        --gpu_memory_fraction 0.25 &
```

> 🔧 **Please update the directory paths (`/user/...`) according to your environment.**


### ✅ 2. Evaluate the Fine-tuned Model

Run the following command to evaluate model performance on your aligned dataset:

```bash
#!/bin/bash

python3 src/validate_on_frozen.py \
    /home/user \
    /home/facenet-master/finetuned_models/20200517-21222 \
    --distance_metric 1 \
    --use_flipped_images \
    --subtract_mean \
    --use_fixed_image_standardization \
    --lfw_pairs /home/pairs_user.txt \
    --lfw_batch_size 78 \
    --lfw_nrof_folds 2
```

This script compares image pairs and computes accuracy, validation rate, FAR, and AUC on your dataset.

### 📥 3. Load and Visualize Results
To print or save the evaluation results:

```
#!/bin/bash

python3 load_result.py
📌 Make sure the results from validate_on_newfaces.py are saved in a readable format before loading.

📂 Repository Structure
facenet-korean/
│
├── src/                 # Core FaceNet code (same as original)
├── fine_tuned_model/   # Checkpoints of the fine-tuned model
├── korean_dataset/     # Korean face images (not included – see below)
├── scripts/            # Training and evaluation scripts
├── README.md           # You are here
└── requirements.txt    # Python dependencies
```

📌 Notes
The Korean face dataset used for fine-tuning is not included due to privacy and licensing constraints.

You may use public datasets such as K-FACE or your own dataset to re-train or test the model.

👤 Author
Maintained and fine-tuned by Soyoung Chae.
Feel free to open issues or pull requests for suggestions and improvements.
