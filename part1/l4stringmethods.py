name = "aung kyaw"
print(name)
print(name[0]) #a
print(name[3]) #g
print(name[8]) #w
print(name[-1]) # w
print(name[-2]) # a
print(name[-8]) # u

# start:end:step 
print(name[0:1]) #a
print(name[0:2]) #au
print(name[0:3]) #aun
print(name[0:4]) #aung

print(name[1:4]) #ung
print(name[1:7]) #ung ky
print(name[1:9]) #aung kyaw

print(name[0:9:1]) #aung kyaw
print(name[0:9:2]) # an yw 
print(name[0:9:3]) # agy

fullname = name # aung kyaw 
fullname = name[:] # aung kyaw 
fullname = name[0:4] # aung
fullname = name[::-1] # wayk gnua
print(fullname) 

# len() 
getlength = len(name) # 9 
print(getlength)

# upper()
text = "hello friend"
print(text.upper()) # HELLO FRIEND

# capitalize()
text = "hello boy"
print(text.capitalize()) # Hello boy

# title()
text = "hello girl"
print(text.title()) # Hello Girl

# lower()
text = "HAVE TO GO"
print(text.lower()) # have to go 
print(text.casefold()) # have to go 

# swapcase() 
todo = "Have To Shop"
print(todo.swapcase()) # hAVE tO sHOP

# strip() / lstrip() / rstrip()
hifi = "   hello friend  "
print(hifi) #    hello friend
print(hifi.strip()) # hello friend
print(hifi.lstrip()) #hello friend
print(hifi.rstrip()) #   hello friend

# replace(old,new) 
greet = "hello friend"
print(greet.replace("friend","sir")) # hello sir
print(greet.replace("Friend","sir")) # hello friend

# startswith() / endswitch()
captial = "Yangon"
print(captial.startswith("Y")) # True
print(captial.startswith("Ya")) # True
print(captial.startswith("y")) # False
print(captial.startswith("ya")) # False

print(captial.endswith("gon")) # True
print(captial.endswith("Yangon")) # True
print(captial.endswith("yangon")) # False

# isupper() / islower()
mobile = "OPPO"
print(mobile.isupper()) # True
print(mobile.islower()) # False

# isdigit() / isalpha() / isnumeric() / isalnum() 
num1 = 528 
num2 = "1500"
num3 = "ten"
num4 = "number ten"
num5 = "hay!"

# print(num1.isdigit()) # error cuz of isdigit() can check only for string 
print(str(num1).isdigit()) # True  
print(num2.isdigit()) # True
print(num3.isdigit()) # False 

print(num2.isalpha()) # False
print(num3.isalpha()) # True

print(num2.isnumeric()) # True
print(num3.isnumeric()) # False

print(num2.isalnum()) # True
print(num3.isalnum()) # True

print(num4.isalnum()) # False (cuz of space)
print(num4.isalnum()) # False (cuz of !)

# isspace() 
middlename = " "
print(middlename) # True

# istitle()
nickname = "Aung Moe"
print(nickname.isspace()) # False
print(nickname.istitle()) # True

# split() 
sayhi = "Hi My Friend"
print(sayhi.split()) # ['Hi', 'My', 'Friend']

# rsplit() 
color = "red,green,blue,white,black"
print(color.rsplit()) # ['red,green,blue,white,black']

# splitlines() 
sayhello = "Hello\nFriend"
print(sayhello.splitlines()) # ['Hello', 'Friend']

# partition() 
sayhello = "Hello Friend Mr.Maung"
print(sayhello.partition(" ")) # ('Hello', ' ', 'Friend Mr.Maung')
print(sayhello.partition(".")) # ('Hello Friend Mr', '.', 'Maung')

# ljust() / rjust() / center() 
post = "Read"
print(post.ljust(10,"-")) # Read------
print(post.rjust(10,"-")) # ------Read
print(post.center(10,"-")) # ---Read---

# format()
city = "Hello {}"
print(city.format("Mandalay")) # Hello Mandalay

city = "Hello {} {}"
print(city.format("Mandalay","Yangon")) # Hello Mandalay Yangon

# format_map() dictionary
student = {"name":"Su Su"}
sayname = "Dear, {name}"
print(sayname.format_map(student)) # Dear, Su Su

print("Hello my {}. Are you {}".format("friend","Aung Aung")) # Hello my friend. Are you Aung Aung

val1 = "sister"
val2 = "Su Su"
print("Hello my {}. Are you {}!".format(val1,val2)) # Hello my sister. Are you Su Su

# count() 
message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s lorem"
countoflorem = message.count("Lorem")
print(countoflorem) # 2

message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy Text ever since the 1500s lorem"
counttotext = message.count("text")
print(counttotext) # 1

# stringmethod 
    # len() 
    # upper() / lower() / capitalize() / title() 
    # swapcase() / strip() / lstrip() / rstrip()
    # replace() 
    # startswitch() / endswitch() 
    # isupper() / islower() / isdigit() / isalpha() / isnumeric() / isalnum / isspace() / istitle()  
    # split() / rsplit() / splitlines()
    # partition() 
    # ljust() / rjust() / center() 
    # format 
    # format_map() 
    # count()