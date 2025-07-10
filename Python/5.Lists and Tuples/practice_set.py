#counting items in tuples
#used count() method
numbers = (2,3,4,4,5,6,7,7,4,3,3,3)
counting = numbers.count(4) #give a number that you want to count...
print(counting)
#Sum of list
items_list = [3,5,4,3,2]
#sum() is used to sum list
sum = sum(items_list)
print(sum)
#Try to changing tuple

items = (34,56,'Anas')
#items[2] = 'Ansi'
print(items)  #Gives error as tuple are immuteable

#Getting marks and sorting them
#we have to change intput before using sort()
#All accourrences is used for multi line cursor editing
marks = []

user_input1 = int(input('Enter marks:'))
marks.append(user_input1)

user_input2 = int(input('Enter marks:') )
marks.append(user_input2)

user_input3 =  int(input('Enter marks:'))
marks.append(user_input3)
marks.sort()
print('Here are some sorted marks...\n',marks)

#Getting input and storing it in list
#intial blank list
fruits = []

user_input1 = input('Enter fruit name :')
fruits.append(user_input1)

user_input2 = input('Enter fruit name :')
fruits.append(user_input2)

user_input3 = input('Enter fruit name :')
fruits.append(user_input3)

print('Here are some fruits...\n',fruits)
 