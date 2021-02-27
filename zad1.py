def func(a):
    c = str(a)
    b = len(a)
    s = ''
    s2 = []
    s = c.split('-')
    summ = int(s[0])
    for i in range(1,len(s)):
        summ = summ - int(s[i])
    print(summ)
    #for i in range(0,b):
     #   if a[i] = '-' or a[i] = '+':
      #      for j in range(0,i):           
       # else:
        #    s2.append(a[i])      
    #print(s)
    #print(s2)
    #print (b)
a = str(input())
func(a)
