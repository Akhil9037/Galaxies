




# not correct
import numpy as np

t = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
v = np.array([4, 6, 16, 34, 60, 94, 136], dtype=float)

n = len(t) - 1          # 6 intervals (even), valid for Simpson's 1/3
h = (t[-1] - t[0]) / n  # h = 2

simpson = (h/3) * (v[0] + 4*np.sum(v[1:n:2]) + 2*np.sum(v[2:n-1:2]) + v[n])

print("Distance (Simpson's 1/3 rule):", simpson)  # 552.0
