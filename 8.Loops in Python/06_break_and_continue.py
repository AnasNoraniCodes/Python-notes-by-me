#use of break,continue and pass

#use of break...it break the loop if condition met
i = 0
for i in range(0,30):
    if (i == 10):
        break
    print(i)    

#use of continue...it skips indentation the loop if condition met
#skip 10...
i = 0
for i in range(0,30):
    if (i == 10):
        continue
    print(i)    

#use of pass...it pass the loop if condition met
#used for to do work later...
i = 0
for i in range(0,30):
    pass