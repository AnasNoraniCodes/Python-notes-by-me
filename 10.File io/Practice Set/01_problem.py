#Finding word in the content
#open file and give value to file variable 
file = open('text_file.txt')
file_data = file.read()   #content is stored in file_data variable

if 'anas' in file_data.lower():  #converts all content to lower case to check acurately

    print('present')
else:
    print('not present')    

    