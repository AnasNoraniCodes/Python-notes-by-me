#Acceseing text file
#open()to open file
our_file = open('02_text_file.txt','r') #r is used to read...
file_data= our_file.read()
#read() is to read file data
print(file_data)
our_file.close()

#file must be closed after use...