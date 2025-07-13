#Sets
#Sets are like dict but for those value that we want to not duplicate
#dict aor sets main main difference ye hai k sets math k set ki trh kam krta hai
#koi bhi value repeat nahi krta
#syntax {} but for empty set we use "set()"

set_of_items = {3,3,3,3,3}
print(type(set_of_items))
print(set_of_items)    #output will be 3 only as it don't dublicate

set_of_marks = set()  #used empty set Syntax
print(type(set_of_marks))
print(set_of_marks)
set_of_marks.add(100)
print(set_of_marks)
