N = int(input())
A = [input() for i in range(N)]
K = int(input())

Catch = [0]*N

k = 0
for i in range(N):
    if A[i] == 'T' and Catch[i] == 0:
        for j in range(k, N):
            if A[j] == 'P' and abs(i-j)<=K:
                Catch[i] = 1
                Catch[j] = 1
                k = j
                break
    #print(Catch)

count = 0
for i in range(N):
    if Catch[i] == 1:
        count += 1

print(count)
