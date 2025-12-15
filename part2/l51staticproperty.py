# Static Property ( Class Variable ) 

# exe 1 
class BankAccount:
    # Static Property
    totalaccounts = 0

    def __init__(self,owner,balance=0):
        self.owner = owner 
        self.balance = balance 
        BankAccount.totalaccounts += 1

accObj1 = BankAccount("Su Myat",100)
accObj2 = BankAccount("Min Min",200)

print("Total bank accounts = ",BankAccount.totalaccounts) # Total bank accounts =  0

# exe 2 
class Car: 
    totalcars = 0 # static property / class property / class property

    def __init__(self,brand):
        self.brand = brand 
        Car.totalcars += 1 

carObj1 = Car("Toyota")
carObj2 = Car("Honda")
carObj3 = Car("Suzuki")

print("Total cars models = ",Car.totalcars) # Total cars models =  3

# exe 3 
class Counter: 
    count = 0 
    
    def __init__(self):
        Counter.count += 1

    @staticmethod 
    def getcount(): 
        return Counter.count # Total Counter count =  3
        # pass # return the None
        # ... # return the None

counterObj1 = Counter()
counterObj2 = Counter()
counterObj3 = Counter()

print("Total Counter count = ",Counter.getcount())

# ==> Custom Static Property 

class customstcproperty:
    def __init__(self,func):
        self.func = func 

        # get(par1(self),par2(obj),par3(cls))
    def __get__(self,obj,cls=None):
        return self.func()

class Greet:
    @customstcproperty
    def sayhi():
        return "Hello Mandalay!"

print(Greet.sayhi) # Hello Mandalay!

# ==> Custom Static Property ( with param )

class stcproperty:
    def __init__(self,func):
        self.func = func 

    def __get__(self,obj,cls=None):
        return self.func(cls)

class NumCounter:
    idx = 100 

    @stcproperty
    def getidx(cls):
        return cls.idx

print(NumCounter.getidx) # 100





