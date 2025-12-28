from functools import reduce
# Reduce list 

#list created
list_data = [3,34,3454,2323,231,23,343,4444,5555]

#function to check the conditions

def greater(a,b):
    if ( a> b):
        return a
    else:
        return b

#By reduce() we can check values in a sequence...
reduced_list = reduce(greater,list_data)
print(reduced_list)