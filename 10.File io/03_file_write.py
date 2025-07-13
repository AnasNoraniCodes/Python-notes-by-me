#Write in file
#we used 'w' for write in files

file_data = '''
            I'm deeply focused on mastering Python,
            Git, and software development workflows.
            With strong goals in Data Science and AI, 
            I actively build projects like smart health apps 
            and structured coding notes.'''

file = open('write_file.txt','w')
file.write(file_data)
file.close()

#file has been created...
