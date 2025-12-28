# Opening files
# if file is not available we have to print error message

try:
    with open('file_01.txt','r') as file_data:  #opens file
        print(file_data.read())                 #read data
except:
    print('File not exists.')                   #if file is not available it give error msg

try:
    with open('file_02.txt','r') as file_data:
        print(file_data.read())
except:
    print('File not exists.')       

try:
    with open('file_03.txt','r') as file_data:
        print(file_data.read())
except  Exception as e:
    print(e)
     


print('\nThannnks')                