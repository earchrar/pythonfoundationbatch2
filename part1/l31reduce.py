# => reduce() 

# syntax 
# from functools import reduce 
# reduce(function,iterable[,initialize])

from functools import reduce

messages = ["Hello","my","friends"]

result1 = reduce(lambda x,y: x+" "+y,messages)
print(result1) # Hello my friends

numbers = [1,2,3,4,5]

result2 = reduce(lambda x,y: x + y,numbers)
print(result2) # 15

result3 = reduce(lambda x,y: x * y,numbers)
print(result3) # 120

# Explaination 
# 1 x 2 = 2 
# 2 x 3 = 6 
# 6 x 4 = 24 
# 24 x 5 = 120

result4 = reduce(lambda x,y: x if x > y else y,numbers)
print(result4) # 5

# Explaination 
# 1 > 2 = 2
# 2 > 3 = 3
# 3 > 4 = 4 
# 4 > 5 = 5 
