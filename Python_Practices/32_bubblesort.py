n = [5,7,3,9,1,67,99,100,18,45]

for i in range(len(n)):
    swapped = False
    for j in range(len(n)-i-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
            swapped = True
    if not swapped:
        break
print(n)