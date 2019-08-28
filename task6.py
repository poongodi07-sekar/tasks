a=[]
print('enter the sides of traingle')
for i in  range(0,3):
    b=int(input())
    a.append(b)
if (a[0] == a[1]) and (a[0]== a[2]):
    print('it is equilatral traingle')
elif (a[0] == a[1]) or (a[1]==a[2]) or (a[0]==a[2]):
    print('it is isosceles triangle')
else:
    print('it is a scalene traingle')
    
    
