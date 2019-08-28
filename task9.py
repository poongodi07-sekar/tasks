a=int(input('enter the number of elemens: '))
l1=[]
l2=[]
l3=[]
print('enter the elemnts with integer values')
for i in range(0,a):
    b=int(input())
    l1.append(b)
print(l1)
print('the even numbers is :')
l2=list(x for x in l1 if x%2==0)
print(l2)
print('the odd numbers are :')
l3=list(x for x in l1 if x%2==1)
print(l3)


