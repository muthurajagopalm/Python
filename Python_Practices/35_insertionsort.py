n = [5,7,3,9,1]

for i in range(1,len(n)):
    curr = n[i]
    print(curr)
    j = i-1
    print(j)
    while j >= 0 and curr < n[j]:
        n[j+1] = n[j]
        j-=1
    n[j+1] = curr
    print(n)
