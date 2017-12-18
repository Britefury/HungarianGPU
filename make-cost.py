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
    parser.add_argument('--max', type=int, default=1000)
    parser.add_argument('--outpath', type=str, default="cost")
    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    
    print("generating %dx%d matrix, max entry %d" % (args.dim, args.dim, args.max), file=sys.stderr)
    cost = np.random.choice(args.max, (args.dim, args.dim)).astype(int)
    
    print("saving %s.npy" % args.outpath, file=sys.stderr)
    np.save(args.outpath, cost)
    
    print("saving %s.txt" % args.outpath, file=sys.stderr)
    np.savetxt(args.outpath + '.txt', cost, fmt='%d', delimiter=' ')

