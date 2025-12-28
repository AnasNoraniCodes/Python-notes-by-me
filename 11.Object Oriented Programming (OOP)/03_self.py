#Self Method

'''     When we use functions in classes than we 
        have to give argument to the function...
        if dont it gives error .
        
'''


#Class created
class Student :
    name = 'Ahmad'  
    group =  'ICS'     # Class attibutes
    paper =  'Computer Science'

    #function in class
    def Greeting(self):  #Always give self parameter 
        print(f'Hello,{self.name}')   #used of self parameter
    @staticmethod  #here we are not using whole object so...static haha
    def Ending() :
        print('\nThanks')   

Ahmad = Student()
 #Instance attibutes

Ahmad.Greeting()    #Self parameter needed
print( Ahmad.group,Ahmad.paper)    
Ahmad.Ending()      #Self parameter not needed

#Self parameter dena lazmi hota hai jub hum functions class 
#main use krte hain...
 
#Satatic se hum just function ko use kr lety hain...chupke se hihih 