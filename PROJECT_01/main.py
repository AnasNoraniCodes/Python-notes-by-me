import random

'''
    Snake = 1
    water = -1
    gun = 0

'''

#Here,we used while loop to play game again and again...
while(True):
#for random number by the computer we used random lib
#so...

#variables declearations
    random_number = random.choice([1,-1,0])  #there is defference b\w choices and choice
    computer_choice = random_number          #used function and inside used list as we needed

    user_choice_str = input('Enter your choice (s,g,w) :')
 

# initial dict created 
    data_dict = {
    's':1,
    'w':-1,
    'g':0
}
    reverse_dict = {
    1:'Snake',
   -1:'Water',
    0:'Gun'
}
    #user str input to int like {1,-1,0}
    user_number = data_dict[user_choice_str]

    c=computer_choice
    u=user_number

    
    print(f'Your choice is {reverse_dict.get(user_number)} and computer choose {reverse_dict.get(computer_choice)}.\nSo,')
    
    if(c==u):
        print('Its a draw,play again...')
         
       
    else:
        if( c==1 and u==0):
            print('You win !')
             
        elif(c==1 and u == -1):
            print('You lose !') 
        elif(c==-1 and u == 1):
            print('You win !')               
        elif(c==-1 and u == 0):
            print('You lose')   
        elif(c==0 and u == -1):
            print('You win')               
        elif(c==0 and u == 1):
            print('You lose')    
        else:'Something went wrong.'
    

 
 
         