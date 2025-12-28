#Exceptions Handling

#try first this code...
try:
    number = int(input('Enter number:'))
    print('Your number is',number)

#we can return error according to our needs
except ValueError as error_msg:
    print('Your are entering a STRING...please enter INTEGERS like this ( 12,34 ).')
    #print(error_msg)    
#if fail then try this code...
except Exception as error_message:
    #Exception is method that through back an error
    print(error_message)


