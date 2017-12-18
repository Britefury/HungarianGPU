#!/usr/bin/env python

"""
    make-cost.py
"""

from __future__ import print_function

import sys
import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dim', type=int, default=1024 << 4)
    parser.add_argument('--max', type=int, default=256)
    parser.add_argument('--outpath', type=str, default="cost.txt")
    
    args = parser.parse_args()
    assert args.max == 256
    
    return args


if __name__ == "__main__":
    args = parse_args()
    cost = np.random.choice(args.max, (args.dim, args.dim)).astype(int)
    np.savetxt(args.outpath, cost, fmt='%d', delimiter=' ')

