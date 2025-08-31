#Employes details

class Employes :
    company = 'Google'   #Class attributes

    def __init__(self,name,address):  #Dunder methods
        self.name=name   #parameters
        self.address = address
p= Employes( 'Anas' , 'Punjab' ) # Values to parameters
print(p.name,p.company,p.address) # Called
