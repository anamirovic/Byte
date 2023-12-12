from enum import Enum
import string
from collections import deque

class CheckerColor(Enum):
    X="X"
    O="O"


class Board:
    def __init__(self, num_of_fields):
        self.num_of_fields = num_of_fields
        #self.fields = []
        self.fields = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['X', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
        self.table_graph = {
            'A1': ['B2'],
            'A3': ['B2', 'B4'],
            'A5': ['B4', 'B6'],
            'A7': ['B6', 'B8'],
            'B2': ['A1', 'A3', 'C1', 'C3'],
            'B4': ['A3', 'A5', 'C3', 'C5'],
            'B6': ['A5', 'A7', 'C5', 'C7'],
            'B8': ['A7', 'C7'],
            'C1': ['B2', 'D2'],
            'C3': ['B2', 'B4', 'D2', 'D4'],
            'C5': ['B4', 'B6', 'D4', 'D6'],
            'C7': ['B6', 'B8', 'D6', 'D8'],
            'D2': ['E1', 'E3', 'C1', 'C3'],
            'D4': ['E3', 'E5', 'C3', 'C5'],
            'D6': ['E5', 'E7', 'C5', 'C7'],
            'D8': ['E7', 'C7'],
            'E1': ['F2', 'D2'],
            'E3': ['F2', 'F4', 'D2', 'D4'],
            'E5': ['F4', 'F6', 'D4', 'D6'],
            'E7': ['F6', 'F8', 'D6', 'D8'],
            'F2': ['E1', 'E3', 'G1', 'G3'],
            'F4': ['E3', 'E5', 'G3', 'G5'],
            'F6': ['E5', 'E7', 'G5', 'G7'],
            'F8': ['E7', 'G7'],
            'G1': ['F2', 'H2'],
            'G3': ['F2', 'F4', 'H2', 'H4'],
            'G5': ['F4', 'F6', 'H4', 'H6'],
            'G7': ['F6', 'F8', 'H6', 'H8'],
            'H2': ['G1', 'G3'],
            'H4': ['G3', 'G5'],
            'H6': ['G5', 'G7'],
            'H8': ['G7'],
        }

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
        self.stacks=0

    
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
        print("1. You")
        print("2. Computer")
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
            
            #print(self.possible_next_moves(position))
            print(self.player_possible_moves('O'))
            #print(self.get_stack_position('B2', 'X'))

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

    def is_game_over(self):
        return self.current_player.stacks > self.max_num_of_stacks // 2

    def player_possible_moves(self, player):
        moves = []
        for pom in range(0, 32):
            if player in self.board.fields[pom]:
                let = pom // 4 + 65
                position = chr(let)
                p = pom // 4
                if p % 2 == 0:
                    number = (pom * 2) % self.board_size + 1
                    position += str(number)
                else:
                    number = (pom * 2 + 1) % self.board_size + 1
                    position += str(number)
                moves.append(self.possible_next_moves(position, player))
        return moves

    def possible_next_moves(self, position, player):
        visited = set()
        queue = deque([(position, 0, [])])
        closest_neighbors = []

        min_length=self.board_size

        while queue:
            current_node, distance, route = queue.popleft()

            if self.check_position(current_node) and min_length >= distance and distance != 0:
                min_length = distance
                closest_neighbors.append((current_node, distance, route + [current_node]))
            else:
                visited.add(current_node)

            for neighbor in self.board.table_graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1, route + [current_node]))

        possible_moves =[]
        for pom in closest_neighbors:
            move = ''
            if chr(ord(position[0]) + 1) == pom[2][1][0]:
                move = 'D'
            else:
                move = 'G'
            
            if (int(position[1:]) + 1) == int(pom[2][1][1:]):
                move = move + 'D'
            else:
                move = move + 'L' 
            for pomm in self.get_stack_position(position, player):
                if (position, pomm, move) not in possible_moves:
                    possible_moves.append((position, pomm, move))
        return possible_moves

    def check_position(self, position):
        letter = position[0].upper()
        number = int(position[1:])
        letNum = (ord(letter) - 65) // 2 
        numNum = number // 2 
        if((ord(letter) - 65)% 2 ==1):
            numNum+= self.board.num_of_fields//2-1
                
        row = letNum*self.board.num_of_fields + numNum
        if('X' in self.board.fields[row] or 'O' in self.board.fields[row]):
            return True
        return False

    def get_stack_position(self, position, player):
        letter = position[0].upper()
        number = int(position[1:])
        letNum = (ord(letter) - 65) // 2 
        numNum = number // 2 
        if((ord(letter) - 65)% 2 ==1):
            numNum+= self.board.num_of_fields//2-1
                
        row = letNum*self.board.num_of_fields + numNum
        positions = [index for index in range(0, 8) if self.board.fields[row][index] == player]
        return positions

    def init(self,player1,player2):
        self.board=Board(self.board_size)
        #self.board.initializeBoard()
        self.current_player=player1
        self.player1=player1
        self.player2=player2
        self.max_num_of_stacks = ((self.board.num_of_fields-2) * (self.board.num_of_fields//2))//8
        

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()

