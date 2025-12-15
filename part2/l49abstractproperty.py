from abc import ABC, abstractclassmethod

class Person(ABC):
    @property
    @abstractclassmethod

    def getrole(self):
        pass 

# personObj = Person() # error 

class Engineer(Person):
    @property
    def getrole(self):
        return "Professional Engineer"
    
enginnerObj = Engineer()
print(enginnerObj.getrole) # Professional Engineer

# => exercise 
class Vehicle(ABC):
    @property 
    def wheels(self):
        return 8
    
    @abstractclassmethod 
    def drive(self):
        pass 

class Car(Vehicle):
    @property 
    def wheels(self):
        return 12 
    
    def drive(self):
        return "Bus is driving on 12 wheels"
    
carObj = Car()
print(carObj.wheels) # 12
print(carObj.drive()) # Bus is driving on 12 wheels

# Abstract Readonly Property 

class Employee(ABC):
    # @property
    @abstractclassmethod
    def id(self):
        pass 

class Developer(Employee):
    def __init__(self,empid):
        self._empid = empid # Protected attribute 

    @property # error
    def id(self):
        return self._empid
    
developerObj = Developer(1001)
print(developerObj.id) # 1001
# developerObj.id = 1002 # <bound method Developer.id of <__main__.Developer object at 0x000002023B316CF0>>
print(developerObj.id) # 1001

# Abstract Read/Write Only Property(Getter/Setter)

class Product(ABC):
    @property 
    @abstractclassmethod
    def price(self):
        pass 

    @price.setter 
    @abstractclassmethod
    def price(self,value):
        pass 

class Book(Product):
    def __init__(self,price):
        self._price = price 

    @property 
    def price(self):
        return self._price
    
    @price.setter 
    def price(self,value):
        if value < 0:
            raise ValueError("Price cannot be negative value")
        self._price = value 

bookObj = Book(100)
print(bookObj.price) # 100
bookObj.price = 50 
print(bookObj.price)
bookObj.price = -10
# print(bookObj.price) # error 



