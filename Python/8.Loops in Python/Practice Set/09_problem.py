#Quiz

user_number = int(input('Enter your number :'))


print('*'*user_number)  #user number jitne stars
print('*',' '*(user_number-4),'*') #start and end pe stars...and center main space
print('*',' '*(user_number-4),'*')
print('*'*user_number,'\n\n')


#Here is the basic type of solution

#Using loop

for current_number in range(1,user_number+1):
    #agr start aor end hai tou complete line pe print kro
    if( current_number == 1 or current_number == user_number):
        print('*'*user_number)
    #Center main spacing k sath print kroo..    
    else:
        print('*',' '*(user_number-4),'*')    
    

#here,we learn about spacing ,shapes and many more...