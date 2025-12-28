# Filter the numbers

#list created
list_data = [5,55,4,65,76,655,4]
#function that will check if number is divisible by 5 or not
def checking_numbers (n):
    if (n%5==0):

        return True
    
#filter get value ( true or false ) from the function by checking list
#and store results in variable...
list_of_numbers = filter(checking_numbers ,list_data)  
#converted in list in must as it give raw values
print(list(list_of_numbers))