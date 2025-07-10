#if elif else statements
#for multiple conditions we use this


user_age = int(input('Enter your age :'))

#if elif else conditions
#if(condition like age==18 or age >=18 and so on...) :
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
#  
#but else used for last statement not checks conditions
else :
#statement
    print('you are not adult')


#if else statement are used for conditional tasks
#if elif else statement are used for multiple conditionals tasks
#elif checks next condition but else not...it prints last statement if program go to end...hahah