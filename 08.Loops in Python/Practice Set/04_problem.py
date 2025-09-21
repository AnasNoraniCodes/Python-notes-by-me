user_number = int(input('Enter your number :'))

for i in range(2,user_number):
    if((user_number%i)==0):
        print(f'{user_number} is divided by {i} and we know number is not prime...')
    else:
        print(f'{user_number} is prime...')
        break

    