#Constructers 

#Class created
class Student :
    name  =  'Ahmad'
    group =  'ICS'     # Class attibutes
    paper =  'Computer Science'

    #Dunder Methods in python
    def __init__(self,name,group,paper):  #self is must...than self.parameter
        self.name = name
        self.group =group
        self.paper= paper
        print('I am using dunder methods here...')
        
#using dunder method we add new values to the defualts values
Ahmad = Student('Anas','2nd year','Maths')  
print(Ahmad.name,Ahmad.group,Ahmad.paper)    

