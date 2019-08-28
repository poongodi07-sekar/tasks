import functools
a=int(input('enter the number of elements: '))
b=[]
print('enter the elements: ')
for i in range(0,a):
    c=int(input())
    b.append(c)
print(b)
d=1
print(functools.reduce(lambda x,y:x*y,b))

    
