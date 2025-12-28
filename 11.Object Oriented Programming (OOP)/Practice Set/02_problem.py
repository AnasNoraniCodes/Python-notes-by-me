#Calculater 

class Calculater:
    
    def __init__(self,number):  #dunder method for taking value of number 
        self.number = number    
    
    def square (self):
        print(f"The square of {self.number} is {self.number*self.number}.")

    def cube (self):
        print(f"The cube of {self.number} is {self.number*self.number*self.number}.")    

    def squareroot (self):
        print(f"The square root of {self.number} is {self.number**1/2}.")  
    @staticmethod
    def greeting(): #no need of self parameter as it is static      
        print('Hello,there!')


value = int(input('Enter your number :'))
calculate =Calculater(value)
#Static method called...
calculate.greeting()
#functions called...
calculate.square()
calculate.cube()
calculate.squareroot()





