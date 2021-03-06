#%%
from functools import lru_cache

@lru_cache
def fib(n):
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2)

for i in range(400):
  print(i, fib(i))
print("done")
