#Checking the greatest number in 4 numbers
#user input
n1 = int(input('Enter number :'))
n2 = int(input('Enter number :'))
n3 = int(input('Enter number :'))
n4 = int(input('Enter number :'))

#condition checking
if( n1>n2 and n1>n3 and n1>n4 ):
    print(f'{n1} is greater than all other numbers ',n2,',',n3,'and',n4,'.')
elif( n2>n1 and n2>n3 and n2>n4 ):
    print(f'{n2} is greater than all other numbers ',n1,',',n3,'and',n4,'.')
elif( n3>n2 and n3>n1 and n3>n4 ):
    print(f'{n3} is greater than all other numbers ',n1,',',n2,'and',n4,'.')
else:
     print(f'{n4} is greater than all other numbers ',n1,',',n2,'and',n3,'.')

#we can use multiple "and" in conditions...    