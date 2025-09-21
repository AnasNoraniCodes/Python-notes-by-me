#lenght of list

#class created
class vector :
    #constructor created
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)   #__len__() is used to get len of list etc

#object created
n1 = vector([1,2,3,4])  #list passed to L
print(len(n1))        