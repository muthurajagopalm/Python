
def two_nums(num,target):
    n = len(num)
    for i in range(n+1):
        for j in range(i+1,n):
            if num[i] + num[j] == target:
                return[i,j]
num = [3,5,6,1,11]
target = 12

print(two_nums(num, target))
