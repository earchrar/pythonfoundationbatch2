# Type of Argument in Python 
# Positional Arguments 
# Keyword Arguments 
# Default Arguments 
# Variable-length Arguments (*args) (Non-keyword Variable Arguments)
# Variable-length Arguments (**kwargs) (keyword Variable Arguments)

# Positional Arguments 
def greet(name,age):
    print(f"Hello friend! My name is {name}, i am {age} years old")

greet("Su Su",23) # Hello friend! My name is Su Su, i am 23 years old
greet(25,"Nu Nu") # Hello friend! My name is 25, i am Nu Nu years old

# Keyword Arguments 
def hifi(name,age):
    print(f"Hello friend! My name is {name}, i am {age} years old")

hifi(name="Min Min",age=25) # Hello friend! My name is Min Min, i am 25 years old
hifi(age=30,name="Nyi Nyi") # Hello friend! My name is Nyi Nyi, i am 30 years old

# Default Arguments 
def hime(name,age=18):
    print(f"Hello friend! My name is {name}, i am {age} years old")

hime("Yamin") # Hello friend! My name is Yamin, i am 18 years old
hime("Thuzar",20) # Hello friend! My name is Thuzar, i am 20 years old

# Variable-length Arguments (*args) (Non-keyword Variable Arguments)
def boys(*args):
    print(args) 

boys("aung aung") # ('aung aung',)
boys("aung aung","kyaw kyaw") # ('aung aung', 'kyaw kyaw')
boys("aung aung","kyaw kyaw","zaw zaw","tun tun") # ('aung aung', 'kyaw kyaw', 'zaw zaw', 'tun tun')
# boys("aung aung",args="kyaw kyaw"); # error when including Keyword Arguments 

def sumresult(*numbers):
    total = sum(numbers)
    print(f"Sum result is = {total}")

sumresult(1,2,3) # Sum result is = 6
sumresult(10,20,30,40,50) # Sum result is = 150

def myfunone(num,*nums):
    print(num) # 1
    print(nums) # (2, 3, 4, 5)

myfunone(1,2,3,4,5)

# ERROR 
# def myfuntwo(*num,nums):
#     print(num) # 1
#     print(nums) # (2, 3, 4, 5)

# myfuntwo(1,2,3,4,5)

# Variable-length Arguments (*kwargs) (keyword Variable Arguments)

def personinfos(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

personinfos(name="Thuzar",age=25)
personinfos(name="Kaung Kaung",professional="Enginner",city="Yangon")

# Exercise ( Combing Different Type of Arguments )

def emailsender(address,*messages,**files):
    print(f"Address = {address}")
    if messages:
        for message in messages:
            print(f"Message = {message}")
    if files: 
        for key,value in files.items():
            print(f"{key} = {value}")

emailsender("dataland@gmail.com","Hello Sir","i want to request vdo records",lesson="Python B1",classdate="25/Nov/2024")

def studentinfos(name,age=18,*hobbies,**infos):
    print(f"Name = {name}")
    print(f"Age = {age}")
    if hobbies:
        for hobbie in hobbies:
            print(f"Hobbies = {hobbie}")
    if infos:
        for key,value in infos.items():
            print(f"{key} = {value}")

studentinfos("Nandar")
studentinfos("Maung Maung",25)
studentinfos("Maung Maung",25,'reading','travelling')
studentinfos("Maung Maung",25,'reading','travelling',city="Bago",profession="Enginner")

def staffinfos(name,age=18,*hobbies,**infos):
    print(f"Name = {name}")
    print(f"Age = {age}")
    if hobbies:
        print(f"Hobbies = {','.join(hobbies)}")
    if infos:
        for key,value in infos.items():
            print(f"{key} = {value}")

staffinfos("Ni Lar",10,'reading','travelling',city="Bago",profession="Enginner")

