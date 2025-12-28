import pyjokes

#Initial print statement

print('Hello,Now we are going to print jokes using\nexternal module called pyjokes.')

#pyjokes library is installed,now we can print jokes.
#creating variable called 'jokes'.

jokes = pyjokes.get_joke()
print(jokes)
