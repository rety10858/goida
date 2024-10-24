import numpy as np
import math
n = int(input())
m = int(input())
a = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        a[i, j] = math.sin(n * i + m * j + 1)
        if a[i, j] < 0:
            a[i, j] = 0
print(a)