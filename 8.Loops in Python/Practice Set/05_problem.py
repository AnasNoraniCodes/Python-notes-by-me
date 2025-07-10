#Sum of numbers

user_number = int(input('Enter your number :'))

i = 0
sum = 0
list = []
while( i <= user_number ):
    list.append(i)
    sum += i
    i += 1

print(f'The sum of {list} is : {sum}')
