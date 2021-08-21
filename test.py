T = int(input("test"))
output = []
while(T>0):
    T -= 1
    N = int(input("N - "))

    if N%7 == 2:
        output.append(1)
        continue
    
    elif N%3 == 1:
        output.append(1)
        continue
    
    else:
        n = 100 - N
        if (n%7 + n%3)%2 == 0:
            output.append(1)
        
print(output)
