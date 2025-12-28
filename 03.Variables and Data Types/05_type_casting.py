#Type Casting

#Type Casting is used to find the type of variables
#Also used to change the type of the variables

marks = 98
type_of_marks = type(marks)
print('This is 98 and its type is :',type_of_marks)

name = 'Anas'
type_of_name = type(name)
print('This is Anas and its type is :',type_of_name)

#we can change the type of the function

hight = '6.1'
type_of_hight = type(hight)
print('This is "6.1" and its type is :',type_of_hight)

#Now let's change it's type.. 

changed_type = float(hight)
print('This is changed type of "6.1" `:',changed_type)