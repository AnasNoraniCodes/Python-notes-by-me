#line number checking...
#file is opend
with open('write_file.txt','r') as file_data:
    lines_data = file_data.readlines()  #read all lines in file

word = 'AI'   
line_number = 1  
#checking word line by line...
for current_line_data in lines_data:
   
    if word in current_line_data:
        print(f'Yes,{word} is present in line number {line_number}.')
        break
    #break the loop and print yes...
    line_number += 1         #line number incrementation
else:
    print('not')
