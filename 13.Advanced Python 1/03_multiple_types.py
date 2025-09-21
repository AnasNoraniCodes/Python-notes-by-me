#For declearing multiple types in lists or tuples etc
#we used this method here...

from typing import List  , Tuple , Union ,Dict

#List of integer and strings
list_data : list[int,str] = [ 34,'Anas']

# Tuple of strings and float
tuple_data :tuple[str,float] = ('Anas',34.45)

# dict of strings and integers
tuple_data :dict[str,int] = { "name" : 'Anas', "age" : 18}