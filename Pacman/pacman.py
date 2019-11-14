class Pacman:
    #set a list of directions with default value   
    directionList = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def place(self, x, y, direction):
        if (x >= 0 and x < 5 and y >= 0 and y < 5):
            self.x = x
            self.y = y
            #use the index of the direction list to represent the facing direction 
            self.direction = self.directionList.index(direction)
        else:
            print("Pacman is not on the grid. \n Please input valid number")

    def move(self):
        #The pacman is facing NORTH and on the grid
        if self.direction == 0 and self.y < 4:
            self.y += 1
        #The pacman is facing EAST and on the grid
        elif self.direction == 1 and self.x < 4:
            self.x += 1
        #The pacman is facing SOUTH and on the grid
        elif self.direction == 2 and self.y > 0:
            self.y -= 1
        #The pacman is facing WEST and on the grid
        elif self.direction == 3 and self.x > 0:
            self.x -= 1
        else:
            print("Pacman has been the edge!")

    def left(self):
        if (self.x >= 0 and self.x < 5 and self.y>= 0 and self.y < 5):
            self.direction -= 1
            if self.direction < 0:
                self.direction %= 4

    def right(self):
        if (self.x >= 0 and self.x < 5 and self.y>= 0 and self.y < 5):
            self.direction += 1
            if self.direction > 3:
                self.direction %= 4

    def report(self):
        print("Output: {0}, {1}, '{2}'".format(self.x, self.y, self.directionList[self.direction]))



def main():
    #1. To initialize a pacman
    #2. This initialized pacman stands for an error 
    #   when user inputs the position out of the grid.
    pacman = Pacman(-1, -1, 0)

    menu = """
    1. PlACE: place a Pacman on grid
    2. MOVE: move the Pacman
    3. LEFT: turn the Pacman Left
    4. RIGHT: turn the Pacman right
    5. REPORT: show the position of Pacman
    6. HELP
    7. EXIT
    """

    instruction = """
    This game is of dimensions 5 units X 5 units. 
    When place the pacman, please follow the standard PLACE: "x y direction" with "SPACE" to seprate.
    !!!ATTENTION: Do not place the x and y more than 5.
    """

    print("MENU: " + menu)

    gameIsOn = True
    while gameIsOn:
        try:
            command = int(input("Choose a number: "))
        except (ValueError, UnboundLocalError):
            command = 0
            print("Not a number")

        if command == 1:
            try:
                x,y,direc = input("PLACE the position and direction: ").split()
                x = int(x)
                y = int(y)
                direc = direc.upper()
                pacman.place(x, y, direc)
            except ValueError:
                print("Invalid input!")
                break

            while True:
                print(menu)
                try:
                    command = int(input("Choose a number: "))
                except ValueError:
                    print("Not a number")
                
                if command == 1:
                    print("Pacman is alread on the grid!")
                elif command == 2:
                    pacman.move()
                elif command == 3:
                    pacman.left()
                elif command == 4:
                    pacman.right()
                elif command == 5:
                    pacman.report()
                    gameIsOn = False
                    break
                else:
                    print("Choose the right number on the menu!")
        elif command == 6:
            print("Instruction: "+ instruction)
            print("MENU"+ menu)
        elif command == 7:
            #exit the game
            gameIsOn = False
        else:
            print("Please choose the 1 to start your game!")
            

if __name__ == '__main__':
    main()