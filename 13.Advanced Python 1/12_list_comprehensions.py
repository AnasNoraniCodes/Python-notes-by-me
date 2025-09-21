#List Comprehensions

my_list = [2,3,4,5,6]  #list created
squared_list = []      #Empty list for squares

# Using for loop
for item in my_list:
    squared_list.append(item*item)  # added sqaure in list
print(squared_list)  # printed


print('\n\nOther way using list comprehensions methods\n\n')
squared_list_using_comprehensions = [item*item for item in my_list]      
print(squared_list_using_comprehensions)