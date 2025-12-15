# Parent Class 
class Verhicle: 
    def __init__(self,brand): 
        self.brand = brand      # instance variable

    def power(self):
        return "Petrol"
    
# Subclass (inherit from Vehicle) 
class EV(Verhicle): 
    def power(self):
        return "Battery"        # Overriding parent method 

carObj = EV("Tesla")
print(carObj.brand)     # Tesla
print(carObj.power())   # Battery

# Using super() 

# exe = 1
class Employee: 
    def task(self):
        return "Frontend Development"
    
class Employeer(Employee):
    def task(self):
        return super().task() + " and specialized frameworks."
    
jobObj = Employeer()
print(jobObj.task())

# exe = 2 
class Person: 
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def detailinfo(self):
        return f"Person Name = {self.name} , Age = {self.age}"

class Student(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def detailinfo(self):
        originalinfo = super().detailinfo()
        return f"{originalinfo}, Subject = {self.subject}"
    
studentObj = Student("Myat Noe",20,"Computer Science")
print(studentObj.detailinfo()) # Person Name = Myat Noe , Age = 20, Subject = Computer Science
        
    
