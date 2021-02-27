def func(a):
    s = ''
    s = a.split()
    s1 = ''
    s2 = ''
    s3 = ''
    otv = ''
    if len(s) > 2:
        s1 = str(s[0])
        s2 = str(s[1])
        s3 = str(s[2])    
        otv = s1 + ' ' + s2[0] + ' ' + s3[0]
        otv = otv.title()
        print(otv)
    else:
        a = a.title()
        print(a)
a = str(input())
func(a)
