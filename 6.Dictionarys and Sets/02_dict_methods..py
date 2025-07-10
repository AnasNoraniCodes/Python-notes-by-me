#Dictoionary Methods


dict_of_marks = {
    'Anas' :100,
    'Ali'  :78 ,
    'jimmy':98 ,

}

print(dict_of_marks['Anas']) # prints value using key
print(dict_of_marks.items()) # returns all items in dict
print(dict_of_marks.keys())  # returns all keys
print(dict_of_marks.values())# returns all values

#And so on...

print(dict_of_marks.get('Harry')) # returns none
#print(dict_of_marks['Harry'])     # returns error