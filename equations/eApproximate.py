"""

L = list of positive integers
N = sum of L
P = product of L

Find L to maximize P given N

"""

# %%
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint as pp

# %%
x = np.arange(1,4,0.000001)
y = x ** (10 / x)
dy = np.diff(y) / np.diff(x)
dx = (x[:-1] + x[1:]) / 2

plt.plot(x,y,dx,dy)

zero = np.where(np.diff(np.sign(dy)))[0][0]
e = np.mean(dx[zero:zero+2])

print("e =", np.e)
print("x =", e)
