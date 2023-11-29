from enum import Enum
import string

class FieldColor(Enum):
    BLACK = "Black"
    WHITE = "White"

field_black=FieldColor.BLACK
field_white=FieldColor.WHITE

class CheckerColor(Enum):
    X="X"
    O="O"

checker_black=CheckerColor.X
checker_white=CheckerColor.O

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
                    for q in range(3):
                        print(" ", end=" ")
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
                    for q in range(3):
                        print(" ", end=" ")
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


class Field:
    pass

    
class Game():
    def __init__(self):
        self.board = None
        self.winner = None

    
    def get_board_size(self):
        while True:
            board_size = int(input("Enter board size (8 or 16): "))
            if board_size in range(8, 17):
                if board_size%2==0:
                    self.board_size = board_size
                    break
                print("Board size have to be even.")
            else:
                print("Invalid board size. Please enter 8 or 16.")
            

    def get_first_player(self):
        print("Choose who plays first: ")
        print("1. O")
        print("2. X")
        return int(input())
    
    def start(self):
        self.get_board_size()
        player1 = Player(checker_white)
        player2 = Player(checker_black)
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
        self.board.drawTable()

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

