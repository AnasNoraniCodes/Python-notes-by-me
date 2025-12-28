#Set Methods
# There are also set method like dict,list and str

user_set = set()   #For empty set
print(user_set)
user_set.add(3)
print(user_set)

s = {1,3,4,5,5,5,55,5,5,5,5,5,5}  #set don't repeats values
print(s)
other_set = {1,3} #small set created
print(other_set.issubset(s))