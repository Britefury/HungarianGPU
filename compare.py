#!/user/bin/env python

"""
    compare.pr
"""

from time import time
import numpy as np
import pandas as pd
from lap import lapjv

t = time()
cost = np.load('./cost.npy')
n = cost.shape[0]
print("load time\t%f" % (time() - t))

t = time()
_, py_solution, _ = lapjv(cost.max() - cost)
print("run time\t%f" % (time() - t))


print("shape\t%d" % n)

print("----")
print("py score\t%d" % cost[(np.arange(n), py_solution)].sum())

gpu_solution = np.loadtxt('./gpu-solution.txt', dtype=int)[:,1]
print("gpu score\t%d" % cost[(np.arange(n), gpu_solution)].sum())

rand = [cost[(np.random.permutation(n), np.arange(n))].sum() for _ in range(1000)]
rand = np.mean(rand).round().astype(int)
print("random\t\t%d" % rand)
