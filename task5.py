a=['january','march','may','july','august','october','december']
b=['april','june','september','november']
c=['february']
i1=str(input('enter a month with full letters: '))
i=i1.lower()
if i in a:
    print('the  number of days in {0} is : 31'.format(i))
elif i in b:
    print('the  number of days in {0} is : 30'.format(i))
elif i in c:
   print('the  number of days in {a} is : 28'.format(i))
else:
   print('please enter the month correctly ,not use short term or number')
