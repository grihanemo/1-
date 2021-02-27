def func(a):
    s = ''
    b = ''
    otv = ''
    s = a.split()
    print(s)
    for i in range(0,len(s)):
        b = str(s[i])
        otv = otv + ' '
        for j in range(0,len(b)):
            if b[j] == '3':
                otv = otv + b[j]
            elif  b[j] == '7':
                otv = otv + b[j]
    otv = otv.split()
    otv2 = ''
    summa = int(0)
    otv4 = ''
    for i in range(0,len(otv)):
        summa = int(0)
        otv2 = str(otv[i])
        for j in range(0,len(otv2)):
            summa = summa + int(otv2[j])
        if summa % 3 == 0 and summa % 7 == 0:
            otv4 = otv4 + otv2 + ' '        
    
    print(otv4)
a = str(input())
func(a)
