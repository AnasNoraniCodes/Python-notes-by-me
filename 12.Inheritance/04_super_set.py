#Super().__init__()

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
        super().__init__()  #but now it also run privious class constructure...
        print('principle class')
    collage_rights = 'Yes'

rights = principle()
print(rights.collage_rights)  #just run class principle constructure...
