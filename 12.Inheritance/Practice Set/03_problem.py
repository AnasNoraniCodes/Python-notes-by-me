# Salary and increment

#class created
class Employee :
    #class attributes
    salary = 100
    increment = (salary/100)*20 
    increment_persantage = 20

    #class property using @property
    #ye salary aor increment lay ga aor new salary return kre ga...
    #jo name property k function ka hota hai wo .setter ka hota hai
    @property
    def SalaryAfterIncrement(self):
        return (self.salary+self.increment)
    
    #usnig setter to get increment
    @SalaryAfterIncrement.setter
    def  Getting_Increment(self,total_salary):
        self.increment = total_salary -(self.salary+self.increment)    



#Object created
e = Employee()
print(e.SalaryAfterIncrement)

e.Getting_Increment = 600
print(e.increment)

 
 
         