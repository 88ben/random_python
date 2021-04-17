from sys import exit, argv
def r(a):
  i = a.find('0')
  if i == -1:
    exit(a)
  for m in '123456789':
    m in[(i-j)%9*(i/9^j/9)*(i/27^j/27|i%9/3^j%9/3) or a[j] for j in range(81)] or r(a[:i]+m+a[i+1:])

r(argv[1])