# Table using list comprehensions

number = int (input('Enter number :'))

Table = [ i*number for i in range(1,11)]  #we used comprehention methed here
print(Table)