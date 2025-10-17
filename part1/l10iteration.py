# => for in loop 
# Iteration a list 

colors = ["red","green","blue"]

for color in colors:
    print(color)

# Iteration a string 

message = "Hello World"
print(len(message)) # 11 

for msg in message:
    print(msg)

# Iteration a dicitionary 

students = {"name":"Su Su","age":20,"city":"Mandalay"}
print(students)
print(students.items()) # dict_items([('name', 'Su Su'), ('age', 20), ('city', 'Mandalay')])

for key in students:
    print(key,students[key])

for key,value in students.items():
    print(key,"=",value) 

# => range() in for in loop 

for x in range(10):
    print(x)

print(f"Outside x value is {x}") # Outside x value is 9  

for y in range(1,5):
    print(y) # 1 to 4

print(f"Outside y value is {y}") # Outside x value is 4  

for p in range(1,10,2):
    print(p) # 1 3 5 7 9 

print(f"Outside x value is {p}") # Outside p value is 9 

# => break and continue 

for i in range(10):
    if i == 5: 
        break # Exit the loop if i is 5
    print(i) # 0 to 4

print(f"Outside i value is {i}") # Outside i value is 5

for q in range(10):
    if q == 5: 
        continue # Skip number 5
    print(q) # 0 1 2 3 4 6 7 8 9 

print(f"Outside q value is {q}") # Outside q value is 9

for j in range(10):
    if j % 2 == 0: 
        continue # Skip even number
    print(j) # 1 3 5 7 9 

print(f"Outside j value is {j}") # Outside j value is 9

# Nested Loops 

staffs = [
    ["aung aung","kyaw kyaw","zaw zaw"],
    ["su su","nu nu","yu yu"],
    ["thidar","nilar","muyar"]
]

# for staff in staffs: 
#     for people in staff:
#         print(people)

# for staff in staffs: 
#     for people in staff:
#         print(people)
#     print()

# for staff in staffs: 
#     for people in staff:
#         print(people,end=" ")

for staff in staffs: 
    for people in staff:
        print(people,end=" ")
    print()

# => While Loop 

idx = 0

while idx < 10:
    print(f"Index : {idx}") # 0 to 9
    idx += 1

print(f"Outside idx value is {idx}") # Outside idx value is 10

count = 0

while count < 10:
    count += 1
    print(f"Index : {count}") # 1 to 10
    
print(f"Outside idx value is {count}") # Outside idx value is 10

# enumerate()
paints = ["red","green","blue"]
print(paints)
print(enumerate(paints)) # <enumerate object at 0x0000023563779B20>

for index,paint in enumerate(paints):
    print(index,"=",paint)

index = 0 

while index < len(paints):
    print(index,"=",paints[index])
    index += 1

# => break continue 

# while True: 
#     username = input("Enter username = ")
#     if(username == "aungaung"):
#         break
#     else:
#         continue

# => and not 

initnum = False 

while not initnum: 
    luckynum = input("Enter you lucky number = ")
    if(luckynum.isdigit() and int(luckynum) > 0):
        initnum = True
        print(f"Your lucky number is = {luckynum}")
    else: 
        print("Invalid Number")
