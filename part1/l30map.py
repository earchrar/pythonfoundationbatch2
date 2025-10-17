# => map() 

# syntax 
# map(function,iterable) 

numbers = [1,2,3,4,5,6,7,8,9,10]

def square(num):
    return num ** 2

result1 = map(square,numbers)
print(list(result1)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

result2 = map(lambda x: x ** 2,numbers)
print(list(result2)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter() vs map() 

result3 = filter(lambda x: x % 2 == 0,numbers)
print(list(result3)) # [2, 4, 6, 8, 10]

result3 = map(lambda x: x % 2 == 0,numbers)
print(list(result3)) # [False, True, False, True, False, True, False, True, False, True]

# converting string to upper , lower , capitalize 

backend = ["php","Nodejs","PYTHON"]

result4 = map(str.upper,backend)
print(list(result4)) # ['PHP', 'NODEJS', 'PYTHON']

result5 = map(str.lower,backend)
print(list(result5)) # ['php', 'nodejs', 'python']

result5 = map(str.casefold,backend)
print(list(result5)) # ['php', 'nodejs', 'python']

result6 = map(str.capitalize,backend)
print(list(result6)) # ['Php', 'Nodejs', 'Python']

# nested list 

nestedlist = [10,20],[30,40],[50,60]

result7 = map(lambda x: x[0]+x[1],nestedlist)
print(list(result7)) # [30, 70, 110]

# with tuple 

tuples = (10,15,20,25,30,35,40,45,50)

result8 = map(lambda x: x / 10,tuples)
print(tuple(result8)) # [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

# with Dicitionary 

students = {"Su Su":18,"Aung Aung":20,"Yamin":16,"Nilar":19}
print(students.items()) # dict_items([('Su Su', 18), ('Aung Aung', 20), ('Yamin', 16), ('Nilar', 19)])

result9 = dict(map(lambda student: (student[0],student[1]*2),students.items()))
print(result9) # {'Su Su': 36, 'Aung Aung': 40, 'Yamin': 32, 'Nilar': 38}

# with set

numbersset = {1,2,3,4,5,6,7,8,9,10}

result11 = set(map(lambda x: x * 2 ,numbersset))
print(result11) # {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

# muti iterables 

num1 = [1,2,3,4]
num2 = [4,5,6,7]

result12 = list(map(lambda x,y: x+y ,num1,num2))
print(result12) # [5, 7, 9, 11]