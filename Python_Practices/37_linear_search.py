def linear(arr, target):

    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1







arr = [3,5,7,9,2,4,1,0]
target = 9
print(linear(arr,target))