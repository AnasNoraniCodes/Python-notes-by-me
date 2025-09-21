#Append and strip at the same time

#function created with two perameters...
def remove_word(list,word):
    #For new list...
    new_list = []
    #loop for checking each item in list...
    for item in list:
        #if item = word than word will skip (like not appended in new list)
        #if item!= word than item will append in new list
        #but without word like this...
        if not(item==word):
            new_list.append(item.strip(word))
            #new list main item append kro but word skip kro
    return new_list   
    #return list also

list_of_names = ['Anas','Anasa','Niasa','asas','as']
user_word = input('Enter your word :')

results = remove_word(list_of_names,user_word)
print(results)
