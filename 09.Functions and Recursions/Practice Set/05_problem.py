#lines patterns

def patterns(n):
    #condition is must
    if(n==0):
        return ''
    else:
        print('*'*n)
        # again call the funtion
        # where the value of n is n-1 
        patterns(n-1)

user_number = int(input('Enter number :'))
results = patterns(user_number)
print(results)

#key points about recursions

'''
     Function call itself to solve subproblem is recursion
     Functoin must be break after some repetetions
     Using if statement like (if (n==o):break) etc...
     
'''