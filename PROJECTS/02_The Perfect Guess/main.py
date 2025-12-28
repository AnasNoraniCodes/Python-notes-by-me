#The Perfect Guess
import random
user_number = -1
number = random.randint(1,100)
user_guesses = 0
print(number)

while ( number != user_number ):
    user_number = int(input("Guess the number : "))
    if(user_number==number):
        break  
    if(user_number > number ):
        print('Lower number please...')
        user_guesses += 1
    elif( user_guesses < number ):
        print('Higher number please...')
        user_guesses += 1
     

print(f'The number is {number} and you guess correctly in {user_guesses} attempts.')