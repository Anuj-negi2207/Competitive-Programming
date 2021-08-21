n = 6
blub = [0]*n

for i in range(1, n):
    print(blub)
    count = 0
    for j in range(i, n):
        if j%i == 0:
            blub[j] = 1 - blub[j]
        if blub[j] == 1:
            count += 1

#method 2
def factors(n):
    fact = [1]
    for i in range(2, n-1):
        if n%i == 0:
            fact.append(i)
    fact.append(n)

    return fact

count = 0
for i in range(n):
    if len(factors(i+1))%2 == 0:
        count += 1

print(n-count)

