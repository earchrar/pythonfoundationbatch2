# => List Comprehension 

# [ expression for item in iterable ]
                        # 0 to 4
squares = [x**2 for x in range(5)]
print(squares) # [0, 1, 4, 9, 16]

# 0 * 2 = 0
# 1 * 2 = 2
# 2 * 2 = 4
# 3 * 2 = 9
# 4 * 2 = 16

evens = [x for x in range(10) if x%2 == 0 ]
print(evens) # [0, 2, 4, 6, 8}

chars = [char for char in "hello world"]
print(chars) # {' ', 'e', 'l', 'h', 'r', 'o', 'w', 'd']

numbers = [1,2,2,3,4,7,5,7]
uniqnumbers = [x for x in numbers]
print(uniqnumbers) # [1, 2, 3, 4, 5, 7]

# => Nested Loops in list comprehension 

                            # 0 to 2            # 0 to 1 
couplenums = [ (x,y) for x in range(3) for y in range(2) ]
print(couplenums) # [(0, 1), (2, 1), (0, 0), (1, 1), (2, 0), (1, 0)]

# x takes value 0 to 2 
# y takes value 0 to 1 

# x=0 y=0  (0,0)
# x=0 y=1  (0,1)
# x=1 y=0  (1,0)
# x=1 y=1  (1,1)
# x=2 y=0  (2,0)
# x=0 y=1  (2,1)


# => Nested list comprehension 

nestnumberarr = [[1,2,3],[40,50,60],[700,800,900]]
print(nestnumberarr) # [[1, 2, 3], [40, 50, 60], [700, 800, 900]]

flatarrs = [y for x in nestnumberarr for y in x]
print(flatarrs) # [1, 2, 3, 40, 50, 60, 700, 800, 900]

# for x in nestnumberarr 
# first iteration x = [1,2,3]
# second iteration x = [40,50,60]
# third iteraction x = [700,800,900]

# for y in x 
# first iteraction x = [1,2,3]. processes y = 1, y = 2 ,y = 3
# second iteraction x = [40,50,60]. processes y = 40, y = 50 , y = 60
# third iteraction x = [700,800,900]. processes y = 700, y = 800 ,y = 900