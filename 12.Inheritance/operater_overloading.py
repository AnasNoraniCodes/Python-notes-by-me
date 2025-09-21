#Operater Overloaded

class Numbers :

    def __init__(self,c_value):
         self.n_value = c_value

    def __add__(self,number):
        return self.n_value + number.n_value     


n1 = Numbers(2)   
n2 = Numbers(2)  

print(n1.n_value+n2.n_value)

 