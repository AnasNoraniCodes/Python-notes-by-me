#Checking greater number using Function

def greater_than(a,b,c):
    if ( a>b and a>c):
        return a
    elif ( b>a  and b>c ):
        return b
    elif ( c >a and c >b ):
        return c    

user_number1 = int(input('Enter your number :'))
user_number2 = int(input('Enter your number :'))
user_number3 = int(input('Enter your number :'))

results = greater_than(user_number1,user_number2,user_number3)
print(f"'{results}' is greater than all other numbers.")