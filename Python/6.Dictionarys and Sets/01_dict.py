#Dictionary is like "key Value Pairs"
#flexible(mutable),indexed,dublicate not allowed
#Lists and tuples are not like that...

#Dictionary
#syntax dict{
#              'name'(key)= marks for example(value)
#              'item'     = value etc
#                  }

dict_of_marks = {
    'Anas' :100,
    'Ali'  :78 ,
    'jimmy':98 ,

}

#Benefits over lists
print(type(dict_of_marks))   #type is dict
print(dict_of_marks)         #whole dict
print(dict_of_marks['jimmy'])#output the value using key

