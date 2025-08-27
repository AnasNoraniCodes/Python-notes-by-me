#Score replacing with high score...
#we need to generate random numbers so...
import random

#function created
def game():
    print('You are playing game.')
    score = random.randint(0,100)   #used for random numbers
    print(f'Your score is {score}.')
#file.io concepts...
    
    # file = open('Highest Score.txt','r')
    # high_score = file.read()
    # file.close()
    with open('Highest Score.txt','r') as file:
        high_score = file.read()

    if( high_score == ''):

        # file = open('Highest Score.txt','w')
        # file.write(str(0))
        # file.close()

        with open('Highest Score.txt','w') as file :
            file.write(str(0))


    if ( score > int(high_score)):


        # file = open('Highest Score.txt','w')
        # file.write(str(score)) 
        # file.close()   
               
        with  open('Highest Score.txt','w') as file :
              file.write(str(score)) 
     


game()    