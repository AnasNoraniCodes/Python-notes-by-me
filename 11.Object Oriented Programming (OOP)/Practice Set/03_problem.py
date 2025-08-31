#Quiz

#class created
class Demo :
    inital_value = 10

#class called
demo = Demo()
print(demo.inital_value)  #prints class attributes
demo.inital_value = 5     #instance attributes created
print(demo.inital_value)  #prints instance attributes as it created

print(Demo().inital_value)#prints class attributes as it dont changes class attributes