#Multiple if statements
user_age = int(input('Enter your age :'))
#first independent if statement
if( user_age % 2 ):
    print('Age is even')

#second dependent if statement    
if( user_age >= 18 ):
   
#space for indentition and then,statement
    print('You are adult now.') 
#second condition
elif( user_age < 0 ):
    print('Invalid age') 
#third condition
elif( user_age == 0 ):
    print('Zero is not correct age...')
#elif used for next condition   
#but else used for last statement not checks conditions
else :
#statement
    print('you are not adult')
#else statement executes only all condition are failed...hmmm
   
