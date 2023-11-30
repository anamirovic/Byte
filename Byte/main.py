from enum import Enum
import string

class CheckerColor(Enum):
    X="X"
    O="O"


class Board:
    def __init__(self, num_of_fields):
        self.num_of_fields = num_of_fields
        self.fields = []

    def initializeBoard(self):
        self.fields = [["." for p in range(9)] for p in range(self.num_of_fields//2)]
        for i in range(self.num_of_fields-2):
            if i % 2 == 0:
                for j in range(self.num_of_fields//2): 
                    newList=["X"] + ["." for p in range(8)]
                    self.fields.append(newList)
            else:
                for j in range(self.num_of_fields//2): 
                    newList=["O"] + ["." for p in range(8)]
                    self.fields.append(newList)
        self.fields+=[["." for p in range(9)] for p in range(self.num_of_fields//2)]
    
    def drawTable(self):
        listNumber = list(range(self.num_of_fields+1))
        listLetters = [letter for letter in string.ascii_uppercase[:self.num_of_fields]]
        for i in range(self.num_of_fields + 1):
            if(i==0):
                print(" ", end="    ")
            else:
                print(i, end="     ")
        print()
        for i in range(self.num_of_fields):
            if i % 2 == 0:
                self.drawEvenRow(i, listLetters)
            else:
                self.drawOddRow(i, listLetters)
            
    def drawEvenRow(self, i, listLetters):
        pom = 0
        for k in range(2, -1, -1):
            if k==1:
                print(listLetters[i], end="  ")
            else:
                print("  ", end=" ")
            for j in range(self.num_of_fields):
                if j%2==0:
                    self.drawSingleElement(self.fields[i * self.num_of_fields//2 + j//2], k*3)
                    pom=1
                else:
                    self.drawSingleEmptyElement()
                    pom =0
            print()

    def drawOddRow(self, i, listLetters):
        pom = 1
        for k in range(2, -1, -1):
            if k==1:
                print(listLetters[i], end="  ")
            else:
                print("  ", end=" ")
            for j in range(self.num_of_fields):
                if j%2!=0:
                    self.drawSingleElement(self.fields[i * self.num_of_fields//2 + j//2], k*3)
                    pom=1
                else:
                    self.drawSingleEmptyElement()
                    pom =0
            print()

    def drawSingleElement(self, lista, start):
        for i in range(start, start+3):
            print(lista[i], end=" ")

    def drawSingleEmptyElement(self):
        for i in range(3):
            print(" ", end=" ")


class Player:
    def __init__(self,checker_color):
        self.checker_color=checker_color
        self.score=0

    
class Game():
    def __init__(self):
        self.board = None
        self.winner = None

    
    def get_board_size(self):
        while True:
            board_size = int(input("Enter board size (8 or 16): "))
            if board_size in [8,10, 16]:
                self.board_size = board_size
                break
            else:
                print("Invalid board size. Please enter 8, 10 or 16.")
            

    def get_first_player(self):
        print("Choose who plays first: ")
        print("1. X")
        print("2. O")
        return int(input())
    
    def start(self):
        self.get_board_size()
        player1 = Player(CheckerColor.X)
        player2 = Player(CheckerColor.O)
        while True:
            first_player_choice = self.get_first_player()
            if first_player_choice == 1: 
                self.init(player1, player2)
                break
            elif first_player_choice == 2:
                self.init(player2, player1)
                break
            else:
                 print("Invalid choice. Please enter 1 or 2.")
        while True:
            self.board.drawTable()
            self.make_move()
        
    def make_move(self):
        while True:
            move_input = input(f"{self.current_player.checker_color.value}'s turn. Enter your move (position stack_place direction): ")
            move_parts = move_input.split()
            
            if len(move_parts) != 3:
                print("Invalid input. Please enter position, stack place, and direction.")
                continue
            
            position, stack_place, direction = move_parts
            
            if not self.is_valid_move(position, stack_place, direction):
                print("Invalid move. Please enter a valid move.")
                continue
            else:
                print("Valid move.")
            
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
    
    def is_valid_move(self, position, stack_place, direction):
        a = self.is_valid_position(position) 
        b = self.is_valid_stack_place(position, stack_place) 
        c = self.is_valid_direction(direction)
        k = 1
        return (
            self.is_valid_position(position) and
            self.is_valid_stack_place(position, stack_place) and
            self.is_valid_direction(direction)
        )
    
    def is_valid_position(self, position):
        letter = position[0].upper()
        number = int(position[1:])
        return 0 <= (ord(letter) - 65) < self.board.num_of_fields and 1 <= number <= self.board.num_of_fields and (((ord(letter) - 65) % 2 == 0 and number % 2 == 1) or ((ord(letter) - 65) % 2 == 1 and number  % 2 == 0))
    
    def is_valid_stack_place(self,position, stack_place):

        letter = position[0].upper()
        number = int(position[1:])
        letNum = (ord(letter) - 65) // 2 
        numNum = number // 2 
        if((ord(letter) - 65)% 2 ==1):
            numNum+= self.board.num_of_fields//2-1
            
        row = letNum*self.board.num_of_fields + numNum
        a = self.board.fields[row]
        if( 0 <= int(stack_place) < 8 and a[int(stack_place)]==self.current_player.checker_color.value):
            return True
        return False
    
    def is_valid_direction(self, direction):
        valid_directions = ["GD", "GL", "DL", "DD"]
        return direction in valid_directions

    def init(self,player1,player2):
        self.board=Board(self.board_size)
        self.board.initializeBoard()
        self.current_player=player1
        self.player1=player1
        self.player2=player2
        

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()

