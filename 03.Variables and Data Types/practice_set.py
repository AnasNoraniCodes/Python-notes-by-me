#Finding the square of the number
number_01 = int(input('Enter number 01 :')) #input num 1
#To find square we can use "a*a" and "a**power like (a**2)" but a^2 is invalid
square_of_number = number_01*number_01 #formula a*a is used here...

print('') #spacing
print('Remainder of numbers is :', square_of_number)
#Finding average of two numbers
number_01 = int(input('Enter number 01 :')) #input num 1
number_02 = int(input('Enter number 02 :')) #input num 2

average_of_numbers = (number_01+number_02)/2 #formula (a+b)/2 is used here...

print('') #spacing
print('Remainder of numbers is :', average_of_numbers)

# Comparision b/w values using comparision operaters
number_01 = int(input('Enter number 01 :')) #input num 1
number_02 = int(input('Enter number 02 :')) #input num 2

is_greater = number_01 > number_02 #formula > is used here...
is_equal = number_01 == number_02 #formula == is used here...
is_less = number_01 < number_02 #formula < is used here...

if is_greater :
    print(number_01,' is greater than ',number_02)
if is_equal :
    print(number_01,' is equal to ',number_02)
if is_less :
    print(number_01,' is less than ',number_02)        
    
 

# Checking type of the variable
input_variable ='Anas'
print(type(input_variable))

#Finding remainder
# " % " is used to find a remainder
number_01 = int(input('Enter number 01 :')) #input num 1
number_02 = int(input('Enter number 02 :')) #input num 2

remainder_of_numbers = number_01%number_02 #formula % is used here...

print('') #spacing
print('Remainder of numbers is :', remainder_of_numbers)


#Addition of two numbers

number_01 = int(input('Enter number 01 :')) #input num 1
number_02 = int(input('Enter number 02 :')) #input num 2

sum_of_numbers = number_01+number_02 #formula

print('') #spacing
print('Sum of numbers is :',sum_of_numbers)