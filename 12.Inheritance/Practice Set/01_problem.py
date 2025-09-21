# 2D and 3D class

#class created
class TwoDVector:

    #constructor created
    def __init__(self , i , j):
        self.i = i 
        self.j = j
    def show(self):
        print(f"The Vector is {self.i}i and {self.j}j.")    
        


#class created
class ThreeDVector(TwoDVector):

    #constructor created
    def __init__(self ,i,j, k):
        super().__init__(i,j)
        self.k = k 
    def show(self):
        print(f"The Vector is {self.i}i , {self.j}j and {self.k}k.") 

#Object created
a = TwoDVector(1,2)
a.show()   #Called show() from 2D to show results
b = ThreeDVector(1,2,3)
b.show()   #Called show() from 3D to show results



        

