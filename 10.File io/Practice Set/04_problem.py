#Copy of the file...
#read content of the file
with open('write_file.txt','r') as file_data:
    content_of_file = file_data.read()
#make a copy of the file
with open('copy_file.txt','w') as file:
    file.write(content_of_file)    
#appent the statement at the end
with open('copy_file.txt','a') as file:
    file.write('\n\n This the copy of the file "write_file.txt".')    


#checking that file are same or not...?
#read content of the file
with open('write_file.txt','r') as file_data:
    content_of_file1 = file_data.read()

#read content of the file
with open('copy_file.txt','r') as file_data:
    content_of_file2 = file_data.read()
#conditions 
if ( content_of_file1 ==  content_of_file2 ) :
    print('Yes,these files are same.')
else:
    print('Not,these files are not same.')     


# To remove all the content of the file...simply write " " in file
# To rename file , copy all the content and paste it in new file and
# delete the privious file...hahaha 