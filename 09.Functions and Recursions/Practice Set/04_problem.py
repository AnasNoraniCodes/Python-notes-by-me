#Recursions

'''
       sum(1) = 1
       sum(2) = 2+1
       sum(3) = 3+2+1
       And also...
       sum(n) = 1+2+3+...+n
       
       sum(n) = 1+2+3+...+n-1+n
       as 1+2+3+...n-1 = (n-1)
       #Formula we get...
       sum(n) = (n-1)+n
'''

def sum(n):
    #we used if here not to go in nagetive...
    #if it go...we get error
    if(n==1):
        return 1
    else:
        return (n-1)+n
    
#we,used while to run it again and again...    
while(True):
        user_input = int(input('Enter your number :'))
        results = sum(user_input)

        print(f'The sum of number is {results}.')  





