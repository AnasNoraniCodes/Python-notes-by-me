#Class Attributes vs Instance Attributes

#Class created
class Student :
    group =  'ICS'     # Class attibutes
    paper =  'Computer Science'

Ahmad = Student()  
print(Ahmad.group,Ahmad.paper)    

#Intance Attibutes
Ahmad.group = 'Medical'
print(Ahmad.group)

#It will always fetch instance attibutes first than class attibutes