#Tuples 
#non-flexible , immuteable just like strings
#syntax (2,4) etc
#only few methods

marks = (2,)   #use this "," if only one item is used initially
print(type(marks))

#we can't change the value of tuple like lists
#but we can create new like strings

passwords = ('anas45','xyz4545',123456,4,5,6,3,3,4)
#using methods
print(passwords.count(3))
print(passwords.index(4))

#these are like lists but immuteable (fixed)
