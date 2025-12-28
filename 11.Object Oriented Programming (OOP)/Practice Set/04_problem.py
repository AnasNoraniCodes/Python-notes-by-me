#Train Tikets updates
import random   # also we can used " from ramdom import radiant"
class Train :
    
    #jo constructor hum yahan bana dety hain wo self k sath niche use ho sakte hain
    def __init__(self,trainNo,fro,to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to

    def TrainNo(sel): #jo parameter yahan hota hai os ke sath init wale use hote hain
        print(f"Your train number is {sel.trainNo}.")    
    def GetStutas(sel):
        print(f"Your train is going from {sel.fro} to {sel.to} .") 
    def GetTime(self):
        print(f"You train is running on time and after {random.randint(20,40)} minutes you will be reached. ")         
        


train_updates = Train( 32 , 'Multan' , 'Lahore')
train_updates.TrainNo()
train_updates.GetStutas()
train_updates.GetTime()        


