import random

class BuzzGame:


    def __init__(self):
        self.difficultySet = {"easy" : 1, "medium" : 2, "hard" : 3}
        self.count = 1
        self.correctNextAnswer = ""
        self.botAnswer = ""
        self.difficulty = self.getDifficulty()  # initialize difficulty
        self.buzz = self.getBuzzNum()           # initialize buzz index
        self.useBot = self.getUseBot()          # initialize use bot

    
    # Game Setup
    def getDifficulty(self):
        # Input - Game difficulty
        while True:
            difficulty = input("Select difficulty: (easy, medium, hard): ").lower()
            if (difficulty != "easy" and difficulty != "medium" and difficulty != "hard"):
                print("Invalid input. Please try again.")
            else:
                break
        return difficulty
    
    def getBuzzNum(self):
        # Input - Game Index
        print("Enter number for game buzz or type \"random\" for a random number: ")
        buzzNums = []

        while len(buzzNums) != self.difficultySet.get(self.difficulty):
            buzz = (input(""))
            if buzz.lower() == "random":
                while True:
                    rand = (random.randint(1, 9))
                    if rand not in buzzNums:
                        buzzNums.append(rand)
                        break
            elif int(buzz) > 0 and int(buzz) < 10:
                buzzNums.append(int(buzz))
            else:
                print("Invalid input. Please try again. ")
            print(f"Current buzz numbers: {buzzNums}.")

        print(f"The game index is: {buzzNums} \n")
        return buzzNums
        
    def getUseBot(self):
        # Input - Game uses bot ?
        print("Play against a bot?\n(\"y\" or \"n\")")

        while True:
            useBot = input("Enter Y or N: ")
            if useBot.lower() == "y":
                useBot = True
                break
            elif useBot.lower() == "n":
                useBot = False
                break
            else:
                print("Invalid input. Please try again.")

        if useBot:
            print("You are playing against a bot.")
        else:
            print("You are not playing against a bot.")
        return useBot

    # Game Logic
    def play(self):
        while True:
            # update correctNextAnswer
            if self.isBuzz(int(self.count + 1)) == True:
                self.correctNextAnswer = "buzz"
            else:
                self.correctNextAnswer = str(int(self.count) + 1)

            # print("correct: " + self.correctNextAnswer)  # <<< cheat code
            
            # update botAnswer -- if use bot
            if (self.useBot):
                if self.isBuzz(int(self.count)) == True:
                    self.botAnswer = "buzz"
                else:
                    self.botAnswer = str(int(self.count))

                print(f"Bot Answer: {self.botAnswer}")
            elif(self.count == 1):
                self.botAnswer = str(int(self.count))
                print(f"Start value: {self.botAnswer}")

            inputVal = str(input("Enter next value: \n"))
            
            if inputVal == self.correctNextAnswer:
                # player got it right
                pass
            else:
                self.gameOver()
                break
            print("-----------------------------------------------------------------------")
            self.count += 1
            if (self.useBot): self.takeTurn()

    def takeTurn(self):
        self.count += 1

    def gameOver(self):
        print("You lost.")    

    def isBuzz(self, input):
        if input in self.buzz: return True
        for index in self.buzz:
            if int(input) % int(index) == 0: return True
        return False

#-------------------------------------------------------------
# On Run
#-------------------------------------------------------------

game = BuzzGame()
game.play()