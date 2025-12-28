#Property decorater

#class created
class Train:
    #class attibutes
    rent = 40
    #self function
    def ticket (self):
        print('Your ticket number is 13.')
    
    #property decorater...
    @property
    #used property decorater to create class property and return something...
    def p_name (self):
        return f"{self.fname} {self.mname} {self.lname}"  #return value to print it later...
    # set p_name value using setter here...
    @p_name.setter
    def p_name (self,value):   #function created to store value of passangers name(p_name)
        print('Setter is running...')
        self.fname = value.split(' ')[0]  #value splited using " " and index diya hai
        self.mname = value.split(' ')[1]
        self.lname = value.split(' ')[2]



#initilization...
train_details = Train()
#class function called...
train_details.ticket()
#class attibutes called...
print(train_details.rent)

#give value to p_name funtion using setter...
train_details.p_name = 'Anas Norani Dev'
print(train_details.fname,train_details.mname,train_details.lname)  #values printed here like class attributes (like rent)