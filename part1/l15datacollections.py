# => Data Collections ( Module Containers ) 

# => Counter ( from collections module ) 
from collections import Counter

getcounts = Counter("Hello World")
print(getcounts) # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})

# => Queues ( from collections module ) 

from collections import deque 

qpersons = deque(["Su Su","Nu Nu","Yu Yu"])

qpersons.append("Tun Tun") #  Add to right end
qpersons.appendleft("Sai Sai") # Add to left start 

# for person in qpersons:
#     print(person)

# Removing elements 
qpersons.pop() # Remove from right end 
qpersons.popleft() # Remove from right end 

for person in qpersons:
    print(person)

# => defaultdict ( from collections module ) 

from collections import defaultdict

items = defaultdict(list)

items["fruits"].append("apple")
items["fruits"].append("mango")
items["fruits"].append("banana")
items["colors"].append("orange")

print(items["fruits"]) # ['apple', 'mango', 'banana']
print(items["colors"]) # ['orange']
print(items["candy"]) # []

numitems = defaultdict(int) 

numitems["val"] += 1 

print(numitems) # defaultdict(<class 'int'>, {'val': 1})
print(numitems["val"]) # 1

# Grouping Items 
groups = defaultdict(list)
foods = [("fruit","apple"),("fruit","orange"),("vegetable","carrot"),("fruit","mango")]

for key,value in foods:
    groups[key].append(value)

print(groups) # defaultdict(<class 'list'>, {'fruit': ['apple', 'orange', 'mango'], 'vegetable': ['carrot']})

numitems = defaultdict(int) 
print(numitems["val"]) # 0
numitems["val"] = 1 
print(numitems["val"]) # 1

# Counting Elements 

colorcounts = defaultdict(int) 
candycolors = ["red","green","blue","green","red","black","green"]

for candycolor in candycolors:
    colorcounts[candycolor] += 1
print(colorcounts) # defaultdict(<class 'int'>, {'red': 2, 'green': 3, 'blue': 1, 'black': 1})

# => OrderedDict ( from collections module ) 

from collections import OrderedDict 

myorders = OrderedDict() 
myorders["num1"] = 100
myorders["num2"] = 200
myorders["num3"] = 300
myorders["num4"] = 400
myorders["num5"] = 500

print(myorders) # OrderedDict({'num1': 100, 'num2': 200, 'num3': 300, 'num4': 400, 'num5': 500})
print(myorders["num2"]) # 200

# Reordering Item 
myorders.move_to_end("num2")
print(myorders) # OrderedDict({'num1': 100, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

# Reordering Item 
del myorders["num3"]
print(myorders) # OrderedDict({'num1': 100, 'num4': 400, 'num5': 500, 'num2': 200})

config = OrderedDict() 
config['host'] = "localhost"
config['port'] = 8080 
config['debug'] = True 

for key,value in config.items():
    print(f"{key} : {value}")

# => namedtuple ( from collections module )

from collections import namedtuple 

LuckyNumbers = namedtuple("LuckyNumbers",["num1","num2","num3"])

getnums = LuckyNumbers(33,66,99)
print(getnums.num1) # 33
print(getnums.num2) # 66
print(getnums.num3) # 99

# exercise with tuple , hard to remember what indexs number represents 
staffs = ("Yu Yu",20,"Developers")
print(staffs[0]) # Yu Yu 
print(staffs[1]) # 20 
print(staffs[2]) # Developers

# namedtuple
Student = namedtuple("Student",["name","age","profession"])
# pupils = Student('Su Su',30,"Enginner")
pupils = Student(name="Su Su",age=30,profession="Enginner")
print(pupils.name) # Su Su
print(pupils.age) # 30
print(pupils.profession) # Enginner

# => ChainMap ( from collections module )

from collections import ChainMap 

dict1 = {"name":"Aye Aye"}
dict2 = {"city":"Yangon"}
getdata = ChainMap(dict1,dict2)
print(getdata) # ChainMap({'name': 'Aye Aye'}, {'city': 'Yangon'})
print(getdata["name"]) # Aye Aye
print(getdata["city"]) # Yangon

# array (from array module)

from array import array 

myarrs = array('i',[10,20,30,40])
print(myarrs) # array('i', [10, 20, 30, 40])

getlength = len(myarrs)
print(getlength) # 4 

print(myarrs[0]) # 10 
print(myarrs[2]) # 30 

myarrs.append(50)
print(myarrs) # array('i', [10, 20, 30, 40, 50])

print(myarrs.index(50)) # 4
print(myarrs.count(20)) # 1

myarrs.insert(1,100)
print(myarrs) # array('i', [10, 100, 20, 30, 40, 50])

myarrs.remove(30)
print(myarrs) # array('i', [10, 100, 20, 40, 50])

for value in myarrs:
    print(value)

myarrs.reverse()
print(myarrs) # array('i', [50, 40, 20, 100, 10])

# queue (from queue module)

from queue import Queue 

qone = Queue() # Queue(0) mean infinite size 
qone.put(400)
qone.put(100)
qone.put(300)

print(qone.get()) # 400 get afer remove data
print(qone.get()) # 100
print(qone.get()) # 300

# Data Collections 
    # Counter 
    # Queus or deque ( appendleft() | popleft() )
    # defaultdict 
    # OrderedDict ( move_to_end() )
    # namedtuple
    # ChainMap
    # array 
    # queue or Queue ( put() | get() )
    # datetime
    # functools | reduce