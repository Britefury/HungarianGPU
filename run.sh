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
# To change size of matrix, need to change it in hungarian.cu, then recompile
# Also, hungarian.cu operates on CHARs, ATM.  So maybe this isn't a totally fair comparison?