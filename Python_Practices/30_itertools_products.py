from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))


cartesian = product(a,b)
print(' '.join(map(str, cartesian)))

