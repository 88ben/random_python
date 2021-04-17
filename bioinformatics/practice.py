# %%
import numpy as np
count = {"A": 0, "C": 0, "G": 0, "T": 0}
count2 = [0, 0, 0, 0]
numbers = [0,1,2,3]
nucleotides = '?AcXgtXCgTca'.upper()

for n in nucleotides:
    if n in count:
        count[n] += 1

print(count)

print(np.array(list(count.values()))/4)
# A, C, G, T = count.values()
# print(A, C, G, T)