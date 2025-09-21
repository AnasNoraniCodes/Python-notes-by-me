#Inheritance

#class created
class Animals :
    pass  #used passed here to pass...we'll work here later
#class inherited from Animals
class Pets(Animals):
    pass # Again pass

#class created inherited from Pets
class Dog (Pets):

    @staticmethod   # As, we dont need self here...
    def Bark():     #self not needed
        print('Bow Bow !')


#Object created 
o = Dog()
o.Bark()         

