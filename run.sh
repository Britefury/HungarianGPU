#!/bin/bash

# run.sh

# rm *txt

# For smaller sizes
# nvcc -Wno-deprecated-gpu-targets -arch=sm_35 -rdc=true -std=c++11 -o hungarian hungarian.cu
# For larger sizes (???)
nvcc -Wno-deprecated-gpu-targets -arch=sm_35 -rdc=true -std=c++11 -Xcompiler -mcmodel=medium -o hungarian hungarian.cu

# Generate random matrix
python make-cost.py

# Run GPU version
time ./hungarian cost.txt

# Compare to CPU version
time python compare.py

# Notes:
#
# For now, to change size of matrix, need to change it in hungarian.cu and recompile
# !! This seems to break above n = 2 ** 14 -- not sure why, may be an easy fix

# Speed (16384 square matrix)
# GPU: 0.8 s
# CPU: 10 s