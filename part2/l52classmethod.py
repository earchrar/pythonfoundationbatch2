# Note : Decleared using the @classmethod decorator 
    # : Take cls as first argument 
    # : use for Alternative Constructors : create different ways to instantiate objects 

# exe 1
class Greeting: 
    @classmethod
    def sayhello(cls):
        print(f"Hello from {cls.__name__}")

Greeting.sayhello() # Hello from Greeting

# exe 2 
class Mobile: 
    network = "5G"

    @classmethod 
    def getconnection(cls):
        return cls.network 

print(Mobile.getconnection()) # 5G

mobileobj:Mobile = Mobile()
print(mobileobj.getconnection()) # 5G

# exe 3 ( static property + classmethod )

class Counter: 
    count = 0

    def __init__(self):
        Counter.count += 1
    
    @classmethod 
    def getcount(cls): # cls refers to the class itself
        return cls.count 

print(Counter.getcount()) # 0 # before instantiation

countObj1 = Counter()
countObj2 = Counter()
countObj3 = Counter()

print(Counter.getcount()) # 3 # after instant also valid , but less common ( for static methods, class method you don't need to create an object )

# exe 4 
class Book: 
    BOOKTYPE = {"HardCover","PaperBack","Ebook"}

    @classmethod
    def booktypevalid(cls,formatname):
        return formatname in cls.BOOKTYPE 

print(Book.booktypevalid("PDF")) # False
print(Book.booktypevalid("Paperback")) # False
print(Book.booktypevalid("Ebook")) # True

# ==> Alternative Constructors 

class Person: 
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    @classmethod 
    def calculateage(cls,name,birthyear):
        currentyear = 2025 
        age = currentyear - birthyear 
        return cls(name,age)

    @classmethod 
    def currentage(cls,name,birthyear):
        from datetime import date 
        currentyear = date.today().year
        age = currentyear - birthyear
        return cls(name,age)

# Normal instant
# personObj1 = Person("Nu Nu",25)
# print(personObj1.name , personObj1.age) # Nu Nu 25

# Using class method as alternative constructors 
personObj2 = Person.calculateage("Yu Yu",1995)
print(personObj2.name , personObj2.age) # Yu Yu 30

personObj2 = Person.currentage("Hla Hla",1996)
print(personObj2.name , personObj2.age) # Hla Hla 29

# => Class Method with Inheritance 
# exe 1 
class Student:
    def __init__(self,name):
        self.name = name 
    
    @classmethod 
    def describe(cls,level):
        return f"A {cls.__name__} studied at {level} level."

class GraduateStudent(Student):
    pass 

print(Student.describe("undergraduate")) # A Student studied at undergraduate level.
print(Student.describe("graduate")) # A Student studied at graduate level.

# exe 2 
class Vehicle():
    vehicletype = "Unknown"

    @classmethod 
    def describe(cls):
        return f"This is a {cls.vehicletype} vehicle." 

class Car(Vehicle):
    vehicletype = "Car"

print(Car.describe()) # This is a Car vehicle.

# exe 3 
class ProLanguage:
    langtype = "Generic"

    @classmethod 
    def describe(cls):
        return f"This is {cls.langtype} Language."

class JavaScript(ProLanguage):
    langtype = "JavaScript"

class Python(ProLanguage):
    langtype = "Python"

print(ProLanguage.describe()) # This is Generic Language.
print(JavaScript.describe()) # This is JavaScript Language.
print(Python.describe()) # This is Python Language.

# => Define Read-Only Property ( @property )

class Employee:
    def __init__(self,name,monthlysalary):
        self.name = name 
        self._monthlysalary = monthlysalary
    
    @property
    def annualsalary(self):
        return self._monthlysalary * 12 

employeeObj = Employee("Zaw Zaw",500)
print(employeeObj.annualsalary) # 6000

# exe 2 ( @property with Getter and Setter )

class Staff: 
    def __init__(self,name):
        self._name = name 
    
    @property 
    def name(self):
        return self._name.upper()

    @name.setter 
    def name(self,newname):
        self._name = newname 

staffObj = Staff("yu yu")
print(staffObj.name) # YU YU
staffObj.name = "Nu Nu"
print(staffObj.name) # NU NU


# Method Type               Decorator                         First Parameter
# Instance Method            None                                self 
# Dunder Method              None                                self 
# Abstract Method            @abstractmethod                     None 
# Static Method              @staticmethod                       None 
# Class Method               @classmethod                        cls 