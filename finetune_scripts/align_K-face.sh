#!/bin/bash

export PYTHONPATH=/home/jspark/lsmm_proj/facenet-master/src
for N in {1..4}; do \
python /home/jspark/lsmm_proj/facenet-master/src/align/align_dataset_mtcnn.py \
/home/jspark/lsmm_proj/facenet-master/datasets/lfw/K-face_mtcnn/ \
/home/jspark/lsmm_proj/facenet-master/datasets/K-face_160 \
--image_size 160 \
--margin 32 \
--random_order \
--gpu_memory_fraction 0.25 \
& done
