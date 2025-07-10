import pyjokes
import pyttsx3
import os

#Problem 1
#Print the Peom in Python

print('\n    Multi lines String...')
print('''
      
       My name is Anas.
       I am doing ICS 1st year in PGC.
       I am also learning Coding skills.

''')

# Here ,we learn ' multi lines string ' as ' multi lines comments '.
#It is used to print statement like poem or paragraph as it is...

print('*****************----------------------******************\n\n')

# Problem 2
#Intall external module and use it in code.
print('\n    External Modules...\n')
print('we are using pyjokes as an external module...')
#intilization of variable called jokes
jokes = pyjokes.get_joke()
print(jokes)

print('we are also using pyttsx3 as an external module...')
#What we write the module convet it into audio...
#Initilization of module called engine

engine = pyttsx3.init()
engine.say('Hey ! How are you ? You are using external module pyttsx3 to convert text into audio`')
engine.runAndWait()

engine = pyttsx3.init()
engine.say('Here is a joke  listen to it bro')
engine.runAndWait()

engine = pyttsx3.init()
engine.say(jokes)
engine.runAndWait()







print('\n\n*****************----------------------******************\n\n')

#Problem 3
#list out your directory using os module

#yahan pe hum ne path diya hai k ye directory list krni hai
directory_path = '/'
#hum ne sari directory ko ek path like contents main list kr diya hai
contents = os.listdir(directory_path)
#yahan pe ek for loop se list print hoi hai
#end pe " : " lagaya hai aor nichy statement likhi hai
for item in contents:
    print(item)
   




