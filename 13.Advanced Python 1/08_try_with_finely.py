#Try with Finally

def data_handling ():
    
    try:
        number = int(input('Enter number:'))
        print('Your number is',number)
        return
    except Exception as error_message:
   
        print(error_message)
        return
    
    finally:
        print('inside finally...')    

        # Always run...even we return value and want to break
        # In try finally print final message at the end always

data_handling()