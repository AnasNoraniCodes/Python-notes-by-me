#Inheritance 
#Type Single Inheritance
#When we created new class for existing class its called inheritance.
#Snytax " class New(Old):"

#Train Tikets updates
import random   
class Train :
    #All functions are here...

    def __init__(self,trainNo,fro,to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to
    def TrainNo(sel): 
        print(f"Your train number is {sel.trainNo}.")    
    def GetStutas(sel):
        print(f"Your train is going from {sel.fro} to {sel.to} .") 
    def GetTime(self):
        print(f"You train is running on time and after {random.randint(20,40)} minutes you will be reached. ")         
        
class TrainAndBus(Train):
    #One function is here but we used inheritance method here...
    @staticmethod
    def Bus():
        print('Bus route is also available...')

train_updates = TrainAndBus( 32 , 'Multan' , 'Lahore')
train_updates.TrainNo()
train_updates.GetStutas()
train_updates.GetTime()    
train_updates.Bus()    

#we created child class from parent class using inheritance...

