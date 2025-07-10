#Factorial
#5! = 1x2x3x4x5

user_input = int(input('Enter your number :'))

product_list = []
product = 1 
#sum = 0 and product = 1 

for item in range(1,user_input+1):  # we plus one here to go to the end of number
    
    product = product * item
    product_list.append(item)

print(product_list)
print(f'The factorial of {user_input} is {product}')