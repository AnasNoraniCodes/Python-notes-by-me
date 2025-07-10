#There are two types of loops
#while loops and for loops

initial_value = 0

while ( initial_value < 10 ):
    print(initial_value)
    initial_value = initial_value+1
    # i += 1 is also correct

print('\n\nSpacing...\n\n')

for initial_value in range(6):
    print(initial_value)
    