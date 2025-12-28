# The keyword "global" is used to set a global variable
# any where in the program...

# a is global varible 
a = 2
print(a)  #print global variable 

def testing ():
    # a is local variable of testing
    # it cannot be used outside the function
    # if we want to use it outside and want to set it global we used "global"

    global a
    a = 12
    print(a)

# a is global varible 
a = 12

print(a)  #print global variable  
testing() #print local variable     


