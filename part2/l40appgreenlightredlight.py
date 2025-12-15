from random import choice 
from time import sleep

class GreenlightRedlight: 
    def __init__(self):
        self.moves = 0 
        self.maxmoves = 5

    def startgame(self):
        print('Welcome to Green Light, Red Light')
        print("Type 'move' when it is Green Light , but stay still (type Enter key) if you see Red Light!")
        print("Type 'exit' to quit.")

        while self.moves < self.maxmoves:
            getlight = choice(["Green Light","Red Light"])
            print(f'{getlight}')

            sleep(2) # Timer for each light 

            if getlight == "Green Light":
                # sleep(2) # Timer , 2 = 2 seconds
                playaction = input("Your action : ").lower() 

                if playaction == "move":
                    self.moves += 1 
                    print(f'Good job! Moves {self.moves}/{self.maxmoves}')
                elif playaction == "exit":
                    print("Thanks for playing!")
                    break 
                else: 
                    print("Game over!!!, You missed out the Green Light.")
                    break
            elif getlight == "Red Light":
                # sleep(3) # Timer , 3 = 3 seconds

                print("Red Light ! Don't Move!")
                playaction = input("Your action : ").lower()

                if playaction == "move":
                    print("Gamer over!!!, You moved on Red Light.")
                elif playaction == "exit":
                    print("Thanks for playing!")
                    break 

        if self.moves >= self.maxmoves:
            print("Congratulation! You won!")

def main() -> None:
    game: GreenlightRedlight = GreenlightRedlight()
    game.startgame() 

if __name__ == "__main__":
    main()