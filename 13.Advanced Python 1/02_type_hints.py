#Type hints

#used type hint with ( variable_name : int = value ) to 
#acces all int functions and methods for  n .
number : int = 5
name : str = 'Anas'

# In functions we used (def f_name ( parameters ) -> str : etc ).
def sum ( a : int , b : int ) -> int:
    return a+b

print(sum(4,5))  #function called