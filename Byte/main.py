from enum import Enum

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
            if board_size in [8, 16]:
                self.board_size = board_size
                break
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

    def init(self,player1,player2):
        self.board=Board(self.board_size)
        self.current_player=player1
        self.player1=player1
        self.player2=player2   
   

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()

