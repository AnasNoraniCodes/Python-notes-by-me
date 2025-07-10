#Hard Quiz...

user_number = int(input('Enter your number :'))
#user_input...
for currrent_number in range(1,user_number+1):
    print(' '*(user_number-currrent_number),end='')
    #space user number se ek kam chaiay...
    #oske baad ek star chaiay
    print('*'*(2*currrent_number-1),end='')
    #star ka har line k baad 2 ka increament chaiay
    #so,current number like 2x(1-1=1),2x(2-1=3),2x(3-1=5)
    #And so on...
    print('')
    #for new line...

    
     
