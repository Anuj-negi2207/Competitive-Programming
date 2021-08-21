import numpy as np

def LIS(Arr, index, compare, count):
    if index == Arr.size:
        return count

    if Arr[index]>Arr[compare]:
        count = LIS(Arr, index+1, index, count+1)
    
    else:
        count = LIS(Arr, index+1, compare, count)

    return count

def LIStest(Arr, n):
    if n<2:
        return 1
    else:
        count = 0
        count = LIS(A, 1, 0, count) + 1
        return count

A = input()
print(A)
print(type(A))

A = np.array(A)
print(A)
print(type(A))

count = LIStest(A, A.size)
    
print(count)