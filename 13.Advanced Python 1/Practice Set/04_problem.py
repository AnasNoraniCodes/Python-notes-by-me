#Error Handling

try:
    a = int(input('Enter number 01 :'))
    b = int(input('Enter number 02 :'))
    print(f'a/b is {a/b}')

  
    
except ZeroDivisionError as v:
      print('Infinite...')
    