#Enumerate
#list created
list_of_students = ['Anas','Ahsan','Awais']
#initial index
index = 0
#for loop
for item in list_of_students:
    print(f"The index is {index} of {item} in list.")
    index += 1  #index plus plus


print('\n\nDifferent approch using Enumerates...!!\n\n')

#Using Enumerates

for index,item in enumerate(list_of_students):
    print(f"The index is {index} of {item} in list.")