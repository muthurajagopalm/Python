n = [5,7,3,9,1,67,99,100,18,45]

for i in range(len(n)):
    min = i

    for j in range(i+1, len(n)):
        if n[j] < n[min]:
            min = j
            n[i], n[min] = n[min], n[i]
print(n)