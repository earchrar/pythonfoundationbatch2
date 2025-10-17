# => Data Containers 

# list 
mylist = [1,2,3,4,5]
print(type(mylist)) # <class 'list'>

# tuple 
mytuple = (1,2,3,4,5)
print(type(mytuple)) # <class 'tuple'>

# dict 
mydict = {"a":1,"b":2,"c":3}
print(type(mydict)) # <class 'dict'>

# set 
myset = {1,2,3,4,5}
print(myset) # {1, 2, 3, 4, 5}
print(type(myset)) # <class 'set'>

dict1 = {}
print(type(dict1)) # <class 'dict'>

set1 = {}
print(type(set1)) # <class 'dict'>

# Create an empty set 
set2 = set()
print(type(set2)) # <class 'set'>

colors = {"red","green","blue","white","black"}
print(colors)

for color in colors:
    print(color)

print("green" in colors) # True
print("steelblue" in colors) # False

fruits = {"apple","orange"}
print(fruits) # {'apple', 'orange'}

# Adding a Single Element 
fruits.add("cherry")
print(fruits) # {'apple', 'orange', 'cherry'}

# Update a Multiple Element []
fruits.update(["mongo","grap"])
print(fruits) # {'apple', 'cherry', 'mongo', 'grap', 'orange'}

# Remove Element 
fruits.remove("orange") # if no element exits ! will be show an error
print(fruits) 

# Remove Element ( using discard() ) 
fruits.discard("red") # if no element exits ! no error
print(fruits) 

fruits.discard("apple") # if no element exits ! no error
print(fruits) # {'mongo', 'grap', 'cherry'}

# Clear Element 
fruits.clear()
print(fruits) # set()

# Frozenset (Immutable of set) 
fornumbers = frozenset([10,20,30,40])
# fornumbers.add(50) # err 
# fornumbers.remove(40) # err 
print(fornumbers) 
print(20 in fornumbers) # True
print(50 in fornumbers) # False

sayhi = "Hello Friend"
print(set(sayhi)) 

set3 = {1,2,3,6,7}
set4 = {3,4,6,5}

# Union Combine ( | )
print(set3 | set4) # {1, 2, 3, 4, 5, 6, 7}
print(set3.union(set4)) # {1, 2, 3, 4, 5, 6, 7}

# Intersetion ( & )
print(set3 & set4) # {3, 6}
print(set3.intersection(set4)) # {3, 6}

# Difference ( - ) 
print(set3 - set4) # {1, 2, 7}
print(set3.difference(set4)) # {1, 2, 7}

print(set4 - set3) # {4, 5}
print(set4.difference(set3)) # {4, 5}

# Symmetric Difference ( ^ )
print(set3 ^ set4) # {1, 2, 4, 5, 7}
print(set3.symmetric_difference(set4)) # {1, 2, 4, 5, 7}

print(set4 ^ set3) # {1, 2, 4, 5, 7}
print(set4.symmetric_difference(set3)) # {1, 2, 4, 5, 7}

# => set comprehension
# { expression for item in iterable condition }
                        # 0 to 4
squares = {x**2 for x in range(5)}
print(squares) # {0, 1, 4, 9, 16}

# 0 * 2 = 0
# 1 * 2 = 2
# 2 * 2 = 4
# 3 * 2 = 9
# 4 * 2 = 16

evens = {x for x in range(10) if x%2 == 0 }
print(evens) # {0, 2, 4, 6, 8}

uniqchars = {char for char in "hello world"}
print(uniqchars) # {' ', 'e', 'l', 'h', 'r', 'o', 'w', 'd'}

numbers = [1,2,2,3,4,7,5,7]
uniqnumbers = {x for x in numbers}
print(uniqnumbers) # {1, 2, 3, 4, 5, 7}

# => Nested Loops in set comprehension 

                            # 0 to 2            # 0 to 1 
couplenums = { (x,y) for x in range(3) for y in range(2)}
print(couplenums) # {(0, 1), (2, 1), (0, 0), (1, 1), (2, 0), (1, 0

# x takes value 0 to 2 
# y takes value 0 to 1 

# x=0 y=0  (0,0)
# x=0 y=1  (0,1)
# x=1 y=0  (1,0)
# x=1 y=1  (1,1)
# x=2 y=0  (2,0)
# x=0 y=1  (2,1)

# Data Containers 
# list / tuple / dict / set = set() 
# add() / update() / remove() / discard() / clear() / frozenset() 
# Union ( | ) / Intersection ( & ) / Difference ( - ) (or) difference() / Symmetric Difference ( ^ ) (or) symmetric_difference 
# set comprehension / Nested Loops in set comprehension 


