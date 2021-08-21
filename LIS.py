import numpy as np

def LIS(Arr, index, compare, count):
    if index == Arr.size:
        return count

    if Arr[index]>Arr[compare]:
        count = LIS(Arr, index+1, index, count+1)
    
    else:
        count = LIS(Arr, index+1, compare, count)

    return count


A = [ 69, 54, 19, 51, 16, 54, 64, 89, 72, 40, 31, 43, 1, 11, 82, 65, 75, 67, 25, 98, 31, 77, 55, 88, 85, 76, 35, 101, 44, 74, 29, 94, 72, 39, 20, 24, 23, 66, 16, 95, 5, 17, 54, 89, 93, 10, 7, 88, 68, 10, 11, 22, 25, 50, 18, 59, 79, 87, 7, 49, 26, 96, 27, 19, 67, 35, 50, 10, 6, 48, 38, 28, 66, 94, 60, 27, 76, 4, 43, 66, 14, 8, 78, 72, 21, 56, 34, 90, 89 ]
n = len(A)
A = np.array(A)
#print(A)
count = 0
if n>1:
    count = LIS(A, 1, 0, count) + 1
    
else:
    count = 1

print(count)