Code = "IEUATROMRTYSAHNMA"
Code = "AHXNGNXUNEXJIGXSI"
Code = "ANINIGGUSHEJN"
n = 4

if n <=1:
    print(Code)

else:  
    Code = list(Code)

    list_n = [0]*len(Code)
    iterator = 0

    upper_index = int(len(Code)/((n-1)*2))
    print(upper_index)

    j = 0
    for i in range(upper_index+1):
        list_n[j] = Code[i]
        j += (n-1)*2

    j= (n-1)
    for i in reversed(range(upper_index)):
        list_n[j] = Code[len(Code)-i-1]
        j += (n-1)*2

    print(list_n)

    count = 0
    flag = 0
    j = upper_index+1
    for i in range(len(Code)):
        if list_n[i] == 0:   
            list_n[i] = Code[j]
            count += 1
            print(Code[j])

            if count%(n-2) == 0:
                j += 1
                flag = 1 - flag
                continue
            
            if flag == 0:
                j += 4
            
            else:
                j -= 4

    while 'X' in list_n:
        list_n.remove('X')

    print(''.join(list_n))
