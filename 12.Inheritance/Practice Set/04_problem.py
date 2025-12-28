#Complex Numbers

#class created
class Complex:

    #constructor created
    def __init__(self,r,i):
        self.r = r
        self.i = i

    #Operater overload using dunder methods
    def __add__(number1,number2):
        return Complex(number1.r+number2.r,number1.i+number2.i)
    def __str__(self):
        return (f"{self.r} + {self.i}i")
        


#object created
n1 =  Complex(7,4)        
n2 =  Complex(4,8)

print(n1+n2)