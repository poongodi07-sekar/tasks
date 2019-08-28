a=str(input('enter the string :'))
b=list(a.split(' '))
c=list((len(i) for i in b))
c1=max(c)
c2=c.index(c1)
print(b)
print('the element with greater length is : {0}'.format(b[c2]))

