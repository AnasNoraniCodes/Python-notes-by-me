#Multiple Inheritance

class ICS :
    
    ics_students = 12
    def ICS_Students(self):
        print(f"In ICS ,there are {self.ics_students} students.")    

class Medical :
    medical_students = 34
    def Medical_Students(self):
        print(f"In Medical ,there are {self.medical_students} students.") 

class SectionStudents(Medical,ICS):
    def students(self):
        print(f'All students are {self.ics_students+self.medical_students}.') 

 
results = SectionStudents()
results.ICS_Students()
results.Medical_Students()
results.students()              

#we used multiple inheritance here
#we used class ics and medical functions in section_students by using inheritance...