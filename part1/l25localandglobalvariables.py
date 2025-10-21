# => Global Variable 

globalval = "I am global"

def myfun1():
    print("Inside function myfun1 = ", globalval)

myfun1() #  I am global
print("Outside function myfun1 = ",globalval)

# => Local Variable 

def myfun2():
    localval = "I am local"
    print("Inside function myfun2 = ", localval)

myfun2() #  I am local
# print(localval) # NameError: name 'localval' is not defined.

# => Same Name for Local and Global Variable 

globalvar = "i am Global"

def myfun3():
    globalvar = "i am Local"
    print("Inside function myfun3 = ", globalvar)

myfun3() #  i am Local
print("Outside function myfun3 = ",globalvar) #  i am Global

# Exercise (including global Keyword and )

msg1 = "Hello Sir, this is global variable"

def funone():
    msg2 = "Hello Students, this is local variable"

    print("Inside function funone = ",msg1)
    print("Inside function funone = ",msg2)

def funtwo():
    msg1 = "Hello Teacher, this is global variable"
    msg2 = "Hello Staffs, this is local variable"

    print("Inside function funtwo = ",msg1)
    print("Inside function funtwo = ",msg2)

def funthree():
    global msg1 # global Keyword
    msg1 = "Hello Boss, this is global variable"
    msg2 = "Hello Employee, this is local variable"

    print("Inside function funthree = ",msg1)
    print("Inside function funthree = ",msg2)

funone() # Sir,Students
funtwo() # Teacher,Staffs

print("Ouside function before funthree , msg1 value = ",msg1) # Sir,

funthree() # Boss,Employee

print("Ouside function before funthree , msg1 value = ",msg1) # Boss,

# => Nested Function and nonlocal Keyword 

def funfour():
    msg3 = "i am msg3 from outside funfive"

    def funfive():
        nonlocal msg3
        msg3 = "i am msg3 Modified by funfive"

    print("Before invoking funfive = ",msg3) 
    funfive()
    print("After invoking funfive = ",msg3)

funfour()


# LocalandGlobalvariables
    # (i). global 
    # (ii). nonlocal 

