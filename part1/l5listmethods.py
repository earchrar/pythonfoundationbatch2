names = ["aung aung","maung maung","su su","yu yu","nandar"]
print(names) # ['aung aung', 'maung maung', 'su su', 'yu yu', 'nandar']

mixdes = [1500,"hello",123.6,True,"world",False]
print(mixdes) # [1500, 'hello', 123.6, True, 'world', False]

print(mixdes[0]) # 1500
print(mixdes[3]) # True
print(mixdes[-1]) # False
print(mixdes[-2]) # world

print(mixdes[0:1]) # [1500]
print(mixdes[0:2]) # [1500, 'hello']
print(mixdes[1:3]) # ['hello', 123.6]
print(mixdes[0:6]) # [1500, 'hello', 123.6, True, 'world', False]

# start:end:step
print(mixdes[0:6:2]) # [1500, 123.6, 'world']
print(mixdes[0:6:3]) # [1500, True]
print(mixdes[1:6:2]) # ['hello', True, False]
print(mixdes[1:6:3]) # ['hello', 'world']

mix2 = mixdes # [1500, 'hello', 123.6, True, 'world', False]
mix2 = mixdes[:] # [1500, 'hello', 123.6, True, 'world', False]
mix2 = mixdes[0:4] # [1500, 'hello', 123.6, True]
mix2 = mixdes[::-1] # [False, 'world', True, 123.6, 'hello', 1500]
print(mix2)

getlength = len(names)
print(getlength) # 5

# overwite / replace

colors = ["red","green","blue"]
print(colors) # ['red', 'green', 'blue']

colors[0] = "pick"
print(colors) # ['pick', 'green', 'blue']

# colors[3] = "silver" # error
# print(colors)  

# append() data from end (Single)
colors.append("white") # ['pick', 'green', 'blue', 'white']
# colors.append("black","violet") # error 

# extend() data from end (Multi)
colors.extend(["gold"]) # ['pick', 'green', 'blue', 'white', 'gold']
colors.extend(["black","violet"]) # ['pick', 'green', 'blue', 'white', 'gold', 'black', 'violet']
print(colors)

# insert(number,value)
colors.insert(0,"steelblue") # ['steelblue', 'pick', 'green', 'blue', 'white', 'gold', 'black', 'violet']
print(colors)

# remove() (remove value and index)
colors.remove("green") # ['steelblue', 'pick', 'blue', 'white', 'gold', 'black', 'violet']
print(colors) 

# pop() (remove from end value and index)
colors.pop() # ['steelblue', 'pick', 'blue', 'white', 'gold', 'black']
print(colors) 

# del (remove value and index)
del colors[1] # ['steelblue', 'blue', 'white', 'gold', 'black']
del colors[1:3] # ['steelblue', 'gold', 'black']
print(colors) 

# clear() 
vals = [1,2,3,4,5]
print(f"Before clear values {vals}") # Before clear values [1, 2, 3, 4, 5]
vals.clear()
print(f"After clear values {vals}") # After clear values []

# sort() 
boys = ["aung aung","zaw zaw","kyaw kyaw","hein min","yae lay","min khant"]
boys.sort()
print(boys) # ['aung aung', 'zaw zaw', 'kyaw kyaw', 'hein min', 'yae lay', 'min khant']

# reverse() 
boys.reverse()
print(boys) # ['zaw zaw', 'yae lay', 'min khant', 'kyaw kyaw', 'hein min', 'aung aung']

nums = [10,115,11,1,50,30,75,25,65,90,110]

nums.sort()
print(nums) # [1, 10, 11, 25, 30, 50, 65, 75, 90, 110, 115]

nums.reverse()
print(nums) # [115, 110, 90, 75, 65, 50, 30, 25, 11, 10, 1]

# count() / index()
ages = [18,25,30,18,30,25,25,20,18,25]
print(ages.index(20)) # 7
print(ages.index(30)) # 2

countof18 = ages.count(18)
print(countof18) # 3 

countof20 = ages.count(20)
print(countof20) # 1 

countof25 = ages.count(25)
print(countof25) # 4 

# nested list 
numbers = [[1,2,3],[40,50,60],[700,800,900]]
print(len(numbers)) # 3
print(numbers[0]) # [1, 2, 3]
print(numbers[1]) # [40, 50, 60]
print(numbers[2]) # [700, 800, 900]
# print(numbers[3]) # error 
print(numbers[2][0]) # 700
print(numbers[2][2]) # 900

numbers.append([1000,2000]) # [[1, 2, 3], [40, 50, 60], [700, 800, 900], [1000, 2000]]
print(numbers)

numbers.pop() # [[1, 2, 3], [40, 50, 60], [700, 800, 900]]
print(numbers)

numbers.pop(1) # [[1, 2, 3], [700, 800, 900]]
print(numbers)

# join() 
greeting = ["Hello","Su Su"]
print(" ".join(greeting)) # Hello Su Su
print("-".join(greeting)) # Hello-Su Su

# List Unpacking 
print(greeting[0]) # Hello
print(greeting[1]) # Su Su

val1,val2 = greeting
print(val1) # Hello
print(val2) # Su Su

# list() , create a new list 
greeting = "Hello Sir"
print(greeting) # Hello Sir
print(list(greeting)) # ['H', 'e', 'l', 'l', 'o', ' ', 'S', 'i', 'r']

# zip(,) ,iterables (such as lists,tuple,string)
arrone = ["10","20","30"]
arrtwo = ["hi","hello","bye"]

createzip = zip(arrone,arrtwo)
print(createzip) # <zip object at 0x0000023D081FB380>

coverttolist = list(createzip)
print(coverttolist) # [('10', 'hi'), ('20', 'hello'), ('30', 'bye')]


# listmethod 
    # overwrite / replace
    # append() / #extend() 
    # pop()
    # insert()
    # remove() 
    # del() 
    # clear()
    # sort()
    # reverse()
    # count()
    # index()
    # join()
    # nested list
    # List Unpacking
    # list()
    # zip(,)