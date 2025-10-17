# => Unpacking Arguments 

def sayhi(name,age):
    print(f"Hello Friend! my name is {name}, i am {age} years old.")

# => Unpacking Positional Arguments

# sayhi("Su Su",30)
args = ("Yu Yu",20)
sayhi(*args) # Hello Friend! my name is Yu Yu, i am 20 years old.

def addingnumbers(a,b,c):
    print(f"Sum Result = {a+b+c}")

addingnumbers(1,2,3); # Sum Result = 6 

tuplenumber = (10,20,30) # Unpack tuple into arguments 
addingnumbers(*tuplenumber) # Sum Result = 60

listnumber = [100,200,300] # Unpack list into arguments 
addingnumbers(*listnumber) # Sum Result = 600

# Unpack keyword argument 
listinfo = {"name":"Hla Hla","age":30}
sayhi(**listinfo) # Hello Friend! my name is Hla Hla, i am 30 years old.

