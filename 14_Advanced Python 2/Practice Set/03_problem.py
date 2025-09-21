#Vertical table of 7

n=int(input('Enter number :'))
# we have to convert it in str first as we printing it as a list
table_list = [ str(n*i) for i in range(1,11)]  #used list comprehension methods
vertical_list = '\n'.join(table_list)

print(vertical_list)