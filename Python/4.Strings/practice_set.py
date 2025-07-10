#Strings are immutable...

#Formating strings using escape sequences.
data_to_be_formated = 'Hey , Anas !' \
                            'How are you? Hope you are' \
                            'doing good and great.' \
                            '       Best of Luck' 
print(data_to_be_formated)
formated_data = 'Hey , Anas !\n' \
                            '\tHow are you? Hope you are\n' \
                            '\tdoing good and great.\n' \
                            '\t       Best of Luck' 
print(formated_data)

#Replacing double space to single space
user_data2 = input("Enter data2 :")
#replacing... 
print('Updated data...')
print(user_data2.replace('  ',' '))
#main string will not changed anyway...


#Detecting double spacing 
user_input = input('Enter data :')
#this str function gives us index..
print(user_input.find('  ')) #we used string function (str.find('..')) to solve a problem

#Chaining is python

letter = '''
         Dear {user_name}.
         You are selected.
         {date}
         '''
#we used chaining to replace raw data to actual data...
#we used string function (str.replace('...')) to replace...
print(letter.replace('{user_name}','Anas').replace('{date}','20 May 2040'))

#Filling of data and name
user_name = input('Enter your name :')
date = input('Enter date :')
#we used f feature to add variables values where we want...
print(f'''
         Dear {user_name}.
         You are selected.
         {date}
         ''')


#Use of "f"
user_name = input('Enter your name :')
print(f"Your name is {user_name}.")  # f is used instead to concatinating str...



 
