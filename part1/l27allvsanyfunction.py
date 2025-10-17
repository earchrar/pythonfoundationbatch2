# => all(iterable)
# Note (truthy) : Non-zero numbers , non-empty , True 
# Note (falsy) : 0 , non , False 

# => any(iterable)
# Note (truthy) : at least one element is turthy

# => List 

boollists = [True,True,True]
print(all(boollists)) # True
print(any(boollists)) # True


boollists = [True,False,True]
print(all(boollists)) # False
print(any(boollists)) # True


numlists = [1,2,3,4,5]
print(all(numlists)) # True
print(any(boollists)) # True

numlists = [1,2,0,4,5]
print(all(numlists)) # False
print(any(boollists)) # True

emptylist = []
print(all(emptylist)) # True
print(any(boollists)) # True

# => Tuple 

booltuple = (True,True,True)
print(all(booltuple)) # True
print(any(boollists)) # True

# => Set 

numset = {1,2,3,4,5}
print(all(numset)) # True
print(any(boollists)) # True

# => Dicitionary 

colordict = {1:'red',2:'green',3:'blue'}
print(all(colordict)) # True
print(any(boollists)) # True

colordict = {1:'red',0:'green',3:'blue'}
print(all(colordict)) # False
print(any(boollists)) # True

# => using Cases 

stringlists = ["red","green","blue"]
print(all(stringlists)) # True
print(any(boollists)) # True

stringlists = ["red","","blue"]
print(all(stringlists)) # False
print(any(boollists)) # True

# => check all numbers are positive 

numlists = [10,20,30,40,50]

checkposit = all(num > 0 for num in numlists)
print(checkposit) # True

numlists = [10,-20,30,40,50]

checkposit = all(num > 0 for num in numlists)
print(checkposit) # False

# Validate a list of conditions 

requiredfields = ["username","email","password"]

users = {
    "username":"su su",
    "email":"susu@gmail.com",
    "password":"123456789"
}

getresult = all(field in users and users[field] for field in requiredfields) # all([True,True,True]) = True
print(getresult) # True

# = Explaination 

requiredfields = ["username","email","password"]

users = {
    "username":"su su",
    "email":"",
    "password":"123456789"
}

getresult = all(field in users and users[field] for field in requiredfields) # all([True,False,True]) = False
print(getresult) # False
