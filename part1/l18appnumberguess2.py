# Number Guess Application 

import random 
from array import array 
from collections import Counter 

winningnum = random.randint(1,10)
# print(winningnum) 

gameleft = 5

# store guess using a set for unique 
guessset = set() 

# store guess using an array 
guessarray = array('i',[])

print(f"You have {gameleft} chance to guess the number between 1 to 10.")

for curnumber in range(1,gameleft+1):
    try:
        guess = int(input(f"Game {curnumber} : Enter your guess number = "))

        # store the guess in the set and array 
        guessset.add(guess)
        guessarray.append(guess)

        if guess == winningnum: 
            print(f"Congratulation! correct number {winningnum} in {curnumber} attempts! ")
            break
        elif guess < winningnum: 
            print("Too low! , Try again")
        else:
            print("Too high! , Try again")
    except ValueError:
        print("Invalid input. Please enter a valid numbers.")

# check if user has used all chances 
    if curnumber == gameleft: 
        print(f"Sorry!, you've used all your chances. The correct winning number is {winningnum}")

guesstuple = tuple(guessarray)
guesscount = Counter(guessarray)

print("Game Result Analysis")
print(f"Your guesses uniquenumber are (unorder) = {guessset}")
print(f"Your guesses numbers are (ordered) = {guesstuple}")
print(f"Frequency of guess numbers are = {guesscount}")

10
10
7
7
3