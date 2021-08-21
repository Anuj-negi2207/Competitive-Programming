Global_currency = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

def change(N):
    Change_value = [0]*len(Global_currency)
    for i in reversed(range(len(Global_currency))):
        value = int(N/Global_currency[i])
        Change_value[i] = value
        N %= Global_currency[i]
    
    return Change_value 

def print_change(Changed):
    for i in reversed(range(len(Global_currency))):
        if Changed[i]>0:
            [print(Global_currency[i], end = '\t') for j in range(Changed[i])]
                
Changed = change(int(input()))
print_change(Changed)