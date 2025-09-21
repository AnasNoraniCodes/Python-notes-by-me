#Raising error with error message

a = int(input('Enter number 01 :'))
b = int(input('Enter number 02 :'))

if ( b == 0 ):

    #we crash the program here it in needed
    #But with error message also...
    raise ZeroDivisionError('Can not divide by 0 .')
else:
    print(f'a/b is {a/b}')