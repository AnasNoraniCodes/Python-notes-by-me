from functools import reduce

# Map
#list created
list_data = [1,2,3,4,5,6,7,8,9]

#lambda method used instead of function
square = lambda x:x*x
#used map to map the list and perform square on each element 
#Also , stored results in list like squared_list
squared_list = map(square,list_data)

#prints all lists
print(list_data)
print(list(squared_list))


# Filter methods
# Function created for checking even numbers
def checking_even (n):
    if (n%2 == 0):
        return True

# if number is even( like function return true ) it store number in even_list
even_list = filter(checking_even,list_data)
print(list(even_list))   


# Reduce Methods
#function created using lambda
sum_of_numbers = lambda a,b : a+b

# reduced give the func and perform it list in a sequence 
#like in this list [1,2,3] it adds 1 and 2 , than result in 3.
reduced_list = reduce(sum_of_numbers,list_data)
print(reduced_list)