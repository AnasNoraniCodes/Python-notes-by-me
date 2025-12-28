#Use of Enumerate

my_list = [1,2,3,4,5,6,7,8,9]

#Enumerate main index aor item both ek sath works krte hain
for index , item in enumerate(my_list):
    if(index>=3 and index <= 6):
        print(item)