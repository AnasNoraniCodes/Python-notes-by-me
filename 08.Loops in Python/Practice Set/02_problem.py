#Greeting to specific persons

list_of_clients = ['Anas','Ahsan','Kaif']
#list created
for name in list_of_clients:  #used name here as name is linked inside the loop
    if(name.startswith('A')): #here,we used linked variable name
        print(f"Hello ,{name}") #if condition met perform this...
        