# => Decorators

# Function Decorator 

def div1(x,y):
    return x/y

print(div1(10,2)) # 5.0 
print(div1(2,10)) # 0.2

def div2(x,y):
    if y > x:
        return y/x
    else:
        return x/y
    
print(div2(10,2)) # 5.0 
print(div2(2,10)) # 5.0

# decorators 

def check(func):
    def inner(x,y):
        if y > x:
            return y/x 
        return func(x,y)
    return inner 

# Method 1
def div3(x,y):
    return x/y 

div4 = check(div3)

print(div4(10,2)) # 5.0 
print(div4(2,10)) # 5.0

# Method 2 
@check
def div5(x,y):
    return x/y

print(div5(10,2)) # 5.0 
print(div5(2,10)) # 5.0

# exercise 

def mydecorators(func):
    def wrapper():
        print("Before the function run")
        func()
        print("After the function run")
    return wrapper

@mydecorators
def sayhi():
    print("Hello , Sir!")

sayhi()

# => Decorators with Arguments 
# using while 

# def sayname(count):
#     def decorator(func):
#         def wrapper(name):
#             x = 0 # init 
#             while x < count: 
#                 func(name)
#                 x += 1 # increment 
#             return wrapper 
#         return decorator

# @sayname(5)
# def greet(name):
#     print(f"Hello , {name} !")

# greet("Yu Yu")

# def talkmyname(count):
#     def decorator(func):
#         def wrapper(name):
#             for _ in range(count):
#                 func(name)
#             return wrapper 
#         return decorator

# @talkmyname(3)
# def greeting(name):
#     print(f"Hello , {name} !")

# greeting("Ni Ni")

# def sumnumbers(count):
#     def decorator(func):
#         def wrapper(*args):
#             for _ in range(count):
#                 func(args)
#             return wrapper
#         return decorator

# @sumnumbers(2)
# def sumresults(numbers):
#     total = sum(numbers)
#     print(f"Sum result is = {total}")

# sumresults(1,2,3,4,5,6,7,8,9,10)

# => Multiple Decorators 

def setuppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def setexclamation(func):
    def wrapper():
        return func() + " !!!"
    return wrapper

@setuppercase
@setexclamation

def sayhello():
    return "hello"

print(sayhello()) # HELLO !!!

# => Multiple Decorators with Arguments 

def setcounter(count):
    def decorator(func):
        def wrapper(name):
            for _ in range(count):
                func(name)
        return wrapper
    return decorator

def prefix(val):
    def decorator(func):
        def wrapper(name):
            print(val,end=" ")
            return func(name)
        return wrapper
    return decorator
    

@setcounter(2)
@prefix("Dear:")
def saygreet(name):
    print(f"Hello , {name}")

saygreet("Kyi Byar")







