# Table using list comprehensions
while(True):
    number = int (input('Enter number :'))

    Table = [ i*number for i in range(1,11)]  #we used comprehention methed here
    print(Table)


    with open('Tables.txt','a') as file_data:
        print(file_data.write(f"Table of {number}:{Table}\n"))
    