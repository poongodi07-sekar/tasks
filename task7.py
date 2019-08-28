a=int(input('enter the number of elements: '))
b=[]
for i in range(0,a):
    l=int(input())
    b.append(l)
b.sort()
print(b)
if (a%2==1):
    c=int(a/2)
    print('the median is : {0}'.format(b[c]))
else:
    c=int(a/2)
    c1=b[c]+b[c-1]]
    print(c1)
    d=c1/2
    print('the median is : {0}'.format(d))

    
    
 
