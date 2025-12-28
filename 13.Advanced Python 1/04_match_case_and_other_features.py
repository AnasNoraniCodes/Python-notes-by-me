#Match Case
#It is like switch statement in C.

def https_stutas(stutas):
    match stutas:
        case 200: #stutas value
            return print('okay its 200')
        case 400: #stutas value
            return print('okay its 400')
        case 600: #stutas value
            return print('okay its 600')
        case _:
            print('Invalid stutas')
        
https_stutas(2500)    

#Some new features

#dict 01 and 02 created
dict_1 = {'a': 1, 'b': 2} 
dict_2 = {'b': 3, 'c': 4} 

# For merging dict we use ( variable_name = dict_name | dict_name )
merged_dict = dict_1 | dict_2 #merged
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4} 

# For opening more than one files at the same time using with()

with ( 
open('file1.txt') as f1, 
open('file2.txt') as f2 
):
    
    # Process files
    pass

