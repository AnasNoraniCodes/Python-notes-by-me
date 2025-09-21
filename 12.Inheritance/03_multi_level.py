#Multi Level Inheritance
 

#Class 1 
class students :
    def __init__(self):
        print('Student class')
    students_rights = 'Yes'
#Class 2
class teacher(students):
    def __init__(self):
        print('teacher class')
    teacher_rights = 'Yes'
#Class 3
class principle(teacher):
    def __init__(self):
        print('principle class')
    collage_rights = 'Yes'

#only one right as it is parent class
print(students().students_rights) 
#two right as it is at level two class   
print(teacher().students_rights,teacher().teacher_rights) 
#all rights as it has all class properties
print(principle().students_rights,principle().teacher_rights,principle().collage_rights) 
   
    
