#Recursions
#use of factorial formula

'''
         factorial(0)=1
         factorial(1)=1
         factorial(2)=2x1
         factorial(3)=3x2x1

         same as,

         factorial(n)=n x n-1 x n-2...2 x 1  # means : if n = 3 than , 3 x 3-1 like 2 x 3-2 like 1  
         So,
         factorial(n)=n x ( n-1 )

         '''

#function created
def factorial(n):
    #Here,if statement is complsoury as it give error...
    if(n==0 or n == 1):
        return 1
    else:
        #used formula and put it equal to "results"
        results = n * factorial(n-1)
        return results

nn = int(input('Enter number :'))
print(factorial(nn))
