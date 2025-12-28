#'a' is used to append str in the file
 
str = '\nThanks'

open_file = open('text_file.txt','a')
open_file.write(str)
open_file.close()

#we append 'Thanks 'in our file using 'a'