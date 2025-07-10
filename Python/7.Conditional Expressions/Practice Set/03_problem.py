#Verification
data_dict = {
    'Anas':True,
    'Ahsan':True,
    'Asad' :True

}

client_name = input('Enter you name :')

if (data_dict.get(client_name) == True):
    print('You are verified.')
else:
    print('Try again...you are not in the system')    
 
'''  first of all ,we created the dict and than get 
     client name...after that we used if condition that if return
     true print verified...otherwise try again...hahah that's funny

'''

#Checking characters in user_input

user_name = input('Enter your name : ')

if(len(user_name)>10):
    print('Character length is more than 10')

else:
    print('Character length is more than 10')    

#key point...we can check any kind of condition in here like len etc
#same as we use it in list...