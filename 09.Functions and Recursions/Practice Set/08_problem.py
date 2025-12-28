#Table for given numbers

def table(n):
    for i in range(1,11):
        results=print(f'{n} X {i} = {n*i}')
    return results
user_number = int(input('Enter number :'))
results = table(user_number)
print(results)  

#Here,is the table formula for every number...
#All done...