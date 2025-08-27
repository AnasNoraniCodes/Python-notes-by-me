#Write in file
#we used 'w' for write in files

file_data = '''
           I'm Anas Norani, a passionate and self-driven
           student currently pursuing ICS at Punjab Group of Colleges.
           Thanks'''

file = open('text_file.txt','w')
file.write(file_data)
file.close()

#file has been created...
