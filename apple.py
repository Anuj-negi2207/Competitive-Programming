apple = 4
x = [1, 0, -1, -1, 0, 0, 1, 1]
y = [0, 1, 0, 0, -1, -1, 0, 0]

sum = 0
i = j = k = l = 0
while(sum<apple):
    sum = abs(i) + abs(j)
    i += x[k]
    j += y[l]
    k += 1
    l += 1

    if k==7 or l == 7:
        sum = 0
        
