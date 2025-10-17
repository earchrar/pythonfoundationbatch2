# => Dictionary Comprehension 

# { key:value expression for item in iterable }
                        # 0 to 4
squares = {x:x**2 for x in range(5)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 0 * 2 = 0
# 1 * 2 = 2
# 2 * 2 = 4
# 3 * 2 = 9
# 4 * 2 = 16

evens = {x:x for x in range(10) if x%2 == 0}
print(evens) # {0: 0, 2: 2, 4: 4, 6: 6, 8: 8}

# => create dictionary from two lists 

keys = ["fullname","age","city","country"]
values = ["Yumon Oo",25,"Mandalay","Myanmar"]

resultdict = {keys[x]:values[x] for x in range(len(keys))}
print(resultdict) # {'fullname': 'Yumon Oo', 'age': 25, 'city': 'Mandalay', 'country': 'Myanmar'}

combinedict = {key:val for key,val in zip(keys,values)}
print(combinedict) # {'fullname': 'Yumon Oo', 'age': 25, 'city': 'Mandalay', 'country': 'Myanmar'}

# => modifying values in a dictionary 

originaldict = {"x":1,"y":2,"z":3}

newdict = {key:val*2 for key,val in originaldict.items()}
print(newdict) # {'x': 2, 'y': 4, 'z': 6}

# => create dictionary from a string 

sayhi = "Hello Word"

charcount = {char:sayhi.count(char) for char in set(sayhi)}
print(charcount) # {'H': 1, 'r': 1, 'o': 2, ' ': 1, 'l': 2, 'W': 1, 'e': 1, 'd': 1}

