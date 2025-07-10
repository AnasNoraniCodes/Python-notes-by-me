#Lists in Loops

list_of_students = [
    'Anas','Ahsan','Awais','Kaif'
]
#initial value is 0
i = 0
while(i<len(list_of_students)): #i as a index initial 0
    print(list_of_students[i])  #print i as a index of list of items
    i+=1
    #after every check the value of i like index should be increased...

#list in for loop
print('\n\nlist in for loops :')
for i in list_of_students:
    print(i)

#tuple in for loops
print('\n\nTuple in for loops :')
tuple_of_students = ( 'Anas','Ahsan','Awais','Kaif') 
for i in tuple_of_students:
    print(i)   


#str in for loops
print('\n\nstring in for loops :')    

name = 'Anas Norani'
for each_item in name:
    print(each_item)


'''So es trh se silicing se aor for and while loops
   se hum values print kr sakty hain '''    