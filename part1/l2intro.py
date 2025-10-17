print("Hello Aung Aung")

# => Arithmetic Operator
    # + Additon 
    # - Subtration 
    # * Multiplication 

    # / Division ( float division )
    # // Floor Division
    # % Modulus  

    # ** Exponentiation

print(20+5)
print(20-5)
print(20*5)
print(20//5) # 4
print(18/5) # 3.6
print(18//5) # 3
print(20%5) # 0
print(2**5) # 0

# => Operator Precedence ( PEMDAS ) ( left to right working ) 
# Parentheses 
# Exponent 
# Multiplication Division (firstin,firstcal)
# Addition Subtration (firstin,firstcal)

print(2+5*4/10-10%2) # 4.0 
# 2+20/10-10%2 
# 2+2.0-10%2 
# 2+2.0-0 
# 4.0 

print((2+5)*4/10-(10%2)) # 2.8 
# 7*4/10-0 
# 28/10
# 2.8

firstname = "aung kyaw"
last_name = "kyaw"
print(firstname)
print(last_name)
print(firstname,last_name)

x = 10
y = 20 
p = '30'
q = "40"

sum1 = x+y
sum2 = p + q
# sum3 = x+q # error

print(sum1) # 30
print(sum2) # 3040
# print(sum3) #error

num1 = 100
num2 = 200.125 
name = "su su"
hascar = True  # ture/TRUE false/FALSE can't use 

print(num1,num2) # 100 200.125
print(type(num1)) # <class 'int'> 
print(type(num2)) # <class 'float'> 
print(type(name)) # <class 'str'> 
print(type(hascar)) # <class 'bool'> 

colors = ["red","green","blue"]
print(colors)
print(type(colors)) # <class 'list'> 

ages = [20,25,30,35]
print(ages)
print(type(ages)) # <class 'list'> 