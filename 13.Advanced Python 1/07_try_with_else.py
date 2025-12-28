# Try with else...

 
try:
    number = int(input('Enter number:'))
    print('Your number is',number)
except Exception as error_message:
   
    print(error_message)

#Now , we are using else with try    
else:
    print('else...as try is successful.')

#agr try run ho gea tou else chaly ga 
#except run hone pe else nahi chalay ga