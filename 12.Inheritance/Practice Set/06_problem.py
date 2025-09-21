#Vectors

#class created
class Vector :
    #constructor created
    def __init__(self,x,y,z):
        #places holder created
        self.x=x
        self.y=y
        self.z=z

    #Operater overload using dunder methods
    def __add__(self,other):   #used to add vector or other objects
                      #first values of first vector and than other as so on...
            results = Vector(self.x+other.x,self.y+other.y,self.z+other.z)
            return results
         #used to  convert it into str form
    def __str__(self):
            results = f'{self.x}i + {self.y}j + {self.z}k'
            return results
    

#Objects are created
vector1 = Vector(2,3,4)    # Values are entered here
vector2 = Vector(5,2,8)   
vector3 = Vector(9,1,6)   

print(vector1+vector2)