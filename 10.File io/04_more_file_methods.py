#File methods...

#line
 
opened_file = open('text_file.txt','r')
line1 = opened_file.readline()  #read one line
 
print(line1,type(line1))      #type of line is str as it read one line

line2 = opened_file.readline()  #read one line
 
print(line2,type(line2))
#lines
  
opened_file = open('text_file.txt','r')
lines = opened_file.readlines()         #read all line
print(lines,type(lines))              #type is list as it read all lines


#using loop
line = opened_file.readline()
while( line != ''):
    print(line)
    line = opened_file.readline()

opened_file.close    