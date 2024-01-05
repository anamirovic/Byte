from enum import Enum
import string
from collections import deque
import copy

class CheckerColor(Enum):
    X="X"
    O="O"


class Board:
    def __init__(self, num_of_fields):
        self.num_of_fields = num_of_fields
        #self.fields = []
        self.fields = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', 'O', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['O', 'X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['O', 'X', 'O', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', 'O', 'O', 'X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.', '.', '.'], ['O', 'X', 'O', 'X', 'O', 'X', 'O', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.', '.', '.', '.'], 
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
    
    def drawTable(self, table=None):
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
                self.drawEvenRow(i, listLetters, self.fields if table is None else table)
            else:
                self.drawOddRow(i, listLetters, self.fields if table is None else table)
            
    def drawEvenRow(self, i, listLetters, table):
        pom = 0
        for k in range(2, -1, -1):
            if k==1:
                print(listLetters[i], end="  ")
            else:
                print("  ", end=" ")
            for j in range(self.num_of_fields):
                if j%2==0:
                    self.drawSingleElement(table[i * self.num_of_fields//2 + j//2], k*3)
                    pom=1
                else:
                    self.drawSingleEmptyElement()
                    pom =0
            print()

    def drawOddRow(self, i, listLetters, table):
        pom = 1
        for k in range(2, -1, -1):
            if k==1:
                print(listLetters[i], end="  ")
            else:
                print("  ", end=" ")
            for j in range(self.num_of_fields):
                if j%2!=0:
                    self.drawSingleElement(table[i * self.num_of_fields//2 + j//2], k*3)
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
        self.score_X = 0
        self.score_O = 0
    
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

    def get_opponent(self):
        print("Choose opponent: ")
        print("1. Player")
        print("2. Computer")
        return int(input())
    
    def start(self):
        self.get_board_size()
        player1 = Player(CheckerColor.X)
        player2 = Player(CheckerColor.O)

        computer = False

        while True:
            opponent = self.get_opponent()
            if opponent == 1: 
                computer = False
                break
            elif opponent == 2:
                computer = True
                break
            else:
                 print("Invalid choice. Please enter 1 or 2.")

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
        
        if not computer:
            while not self.is_game_over():
                self.board.drawTable()
                self.make_move()
        else:
            while not self.is_game_over():
                if self.current_player.checker_color == CheckerColor.X:
                    self.board.drawTable()
                    self.make_move()
                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1
                else:
                    tabla = copy.deepcopy(self.board.fields)
                    info = (self.score_O, self.score_X, tabla)
                    potez = self.minimax(info, 9, True)
                    print("Computer move: ", potez)
                    new_info = (info[0], info[1], self.board.fields)
                    self.computer_make_move(potez[0], "O", new_info, True)
                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def minimax(self, info, dubina, moj_potez, alpha=(None, -10), beta=(None, 10)):
        if moj_potez:
            return self.max_value(info, dubina, alpha, beta)
        else:
            return self.min_value(info, dubina, alpha, beta)

    def min_value(self, info, depth, alpha, beta, move=None):
        #provera za kraj
        if self.check_end(info) != 0:
            return (move, self.check_end(info))
        moves=self.player_possible_moves(self.current_player.checker_color.value, info[2])#ne valja treba da se filtriraju potezi
        moves_list = [pom for pom in moves if len(pom)!=0]
        if depth==0 or moves_list is None or len(moves_list)==0:
            pom = (move, self.rate(info))
            #print(pom)
            return pom
        else:
            for moves in moves_list:
                for s in moves:
                    info_save=info
                    beta = min(beta, self.max_value(self.computer_make_move(s, "X", info_save), depth-1, alpha, beta, s if move is None else move), key=lambda x: x[1])
                    if beta[1] <= alpha[1]:
                        return alpha
        return beta
    
    def max_value(self, info, depth, alpha, beta, move=None):
        #provera za kraj
        if self.check_end(info) != 0:
            return (move, self.check_end(info))
        moves=self.player_possible_moves(self.current_player.checker_color.value, info[2])#ne valja treba da se filtriraju potezi
        moves_list = [pom for pom in moves if len(pom)!=0]
        if depth==0 or moves_list is None or len(moves_list)==0:
            pom = (move, self.rate(info))
            #print(pom)
            return pom
        else:
            for moves in moves_list:
                for s in moves:
                    info_save=info
                    alpha = max(alpha, self.min_value(self.computer_make_move(s, "O", info_save), depth-1, alpha, beta, s if move is None else move), key=lambda x: x[1])
                    if alpha[1] >= beta[1]:
                        return beta
        return alpha

    def check_end(self, info):
        if info[0] > (self.max_num_of_stacks // 2):
            return 10
        elif info[1] > (self.max_num_of_stacks // 2):
            return -10
        return 0

    def rate(self, info):
        value = 0

        if info[0] > info[1]:
            return 10
        
        vel = self.board_size // 2
        for j in range(0, self.board_size, 2):
            for i in range(0, vel):
                stack_size = 9 - info[2][j*vel+i].count(".") #velicina steka na trenutnom polju
                o_stack_position = [index for index, element in enumerate(info[2][j*vel+i]) if element == "O"]
                if stack_size > 0:
                    if j*vel+i-vel >= 0:
                        gd_size = 9 - info[2][j*vel+i-vel].count(".") #velicina steka gore desno
                        if gd_size > 0:
                            if info[2][j*vel+i][stack_size-1] == "O":
                                for index in o_stack_position:
                                    if gd_size + (stack_size - index) == 8:
                                        return 10
                                    elif gd_size + (stack_size - index) < 8:
                                        if gd_size + (stack_size - index) > value:
                                            value = gd_size + (stack_size - index)
                            else:
                                for index in o_stack_position:
                                    if gd_size + (stack_size - index) == 8:
                                        value = -10
                                    elif gd_size + (stack_size - index) < 8:
                                        if -(gd_size + (stack_size - index)) > value:
                                            value = -(gd_size + (stack_size - index))
                    elif j*vel+i-vel-1 >= 0:
                        gl_size = 9 - info[2][j*vel+i-vel-1].count(".") #velicina steka gore levo
                        if gl_size > 0:
                            if info[2][j*vel+i][stack_size-1] == "O":
                                for index in o_stack_position:
                                    if gl_size + (stack_size - index) == 8:
                                        return 10
                                    elif gl_size + (stack_size - index) < 8:
                                        if gl_size + (stack_size - index) > value:
                                            value = gl_size + (stack_size - index)
                            else:
                                for index in o_stack_position:
                                    if gl_size + (stack_size - index) == 8:
                                        value = -10
                                    elif gl_size + (stack_size - index) < 8:
                                        if -(gl_size + (stack_size - index)) > value:
                                            value = -(gl_size + (stack_size - index))
                    elif j*vel+i+vel-1 <= ((self.board_size * self.board_size) // 2):
                        dl_size = 9 - info[2][j*vel+i+vel-1].count(".") #velicina steka dole levo
                        if dl_size > 0:
                            if info[2][j*vel+i][stack_size-1] == "O":
                                for index in o_stack_position:
                                    if dl_size + (stack_size - index) == 8:
                                        return 10
                                    elif dl_size + (stack_size - index) < 8:
                                        if dl_size + (stack_size - index) > value:
                                            value = dl_size + (stack_size - index)
                            else:
                                for index in o_stack_position:
                                    if dl_size + (stack_size - index) == 8:
                                        value = -10
                                    elif dl_size + (stack_size - index) < 8:
                                        if -(dl_size + (stack_size - index)) > value:
                                            value = -(dl_size + (stack_size - index))
                    elif j*vel+i+vel <= ((self.board_size * self.board_size) // 2):
                        dd_size = 9 - info[2][j*vel+i+vel].count(".") #velicina steka dole desno
                        if dd_size > 0:
                            if info[2][j*vel+i][stack_size-1] == "O":
                                for index in o_stack_position:
                                    if dd_size + (stack_size - index) == 8:
                                        return 10
                                    elif dd_size + (stack_size - index) < 8:
                                        if dd_size + (stack_size - index) > value:
                                            value = dd_size + (stack_size - index)
                            else:
                                for index in o_stack_position:
                                    if dd_size + (stack_size - index) == 8:
                                        value = -10
                                    elif dd_size + (stack_size - index) < 8:
                                        if -(dd_size + (stack_size - index)) > value:
                                            value = -(dd_size + (stack_size - index))

        for j in range(1, self.board_size, 2):
            for i in range(0, vel):
                stack_size = 9 - info[2][j*vel+i].count(".") #velicina steka na trenutnom polju
                o_stack_position = [index for index, element in enumerate(info[2][j*vel+i]) if element == "O"]
                if stack_size > 0:
                    if j*vel+i-vel+1 > 0:
                        gd_size = 9 - info[2][j*vel+i-vel+1].count(".") #velicina steka gore desno
                        if gd_size > 0:
                            if info[2][j*vel+i][stack_size-1] == "O":
                                for index in o_stack_position:
                                    if gd_size + (stack_size - index) == 8:
                                        return 10
                                    elif gd_size + (stack_size - index) < 8:
                                        if gd_size + (stack_size - index) > value:
                                            value = gd_size + (stack_size - index)
                            else:
                                for index in o_stack_position:
                                    if gd_size + (stack_size - index) == 8:
                                        value = -10
                                    elif gd_size + (stack_size - index) < 8:
                                        if -(gd_size + (stack_size - index)) > value:
                                            value = -(gd_size + (stack_size - index))
                    elif j*vel+i-vel >= 0:
                        gl_size = 9 - info[2][j*vel+i-vel].count(".") #velicina steka gore levo
                        if gl_size > 0:
                            if info[2][j*vel+i][stack_size-1] == "O":
                                for index in o_stack_position:
                                    if gl_size + (stack_size - index) == 8:
                                        return 10
                                    elif gl_size + (stack_size - index) < 8:
                                        if gl_size + (stack_size - index) > value:
                                            value = gl_size + (stack_size - index)
                            else:
                                for index in o_stack_position:
                                    if gl_size + (stack_size - index) == 8:
                                        value = -10
                                    elif gl_size + (stack_size - index) < 8:
                                        if -(gl_size + (stack_size - index)) > value:
                                            value = -(gl_size + (stack_size - index))
                    elif j*vel+i+vel <= ((self.board_size * self.board_size) // 2):
                        dl_size = 9 - info[2][j*vel+i+vel].count(".") #velicina steka dole levo
                        if dl_size > 0:
                                if info[2][j*vel+i][stack_size-1] == "O":
                                    for index in o_stack_position:
                                        if dl_size + (stack_size - index) == 8:
                                            return 10
                                        elif dl_size + (stack_size - index) < 8:
                                            if dl_size + (stack_size - index) > value:
                                                value = dl_size + (stack_size - index)
                                else:
                                    for index in o_stack_position:
                                        if dl_size + (stack_size - index) == 8:
                                            value = -10
                                        elif dl_size + (stack_size - index) < 8:
                                            if -(dl_size + (stack_size - index)) > value:
                                                value = -(dl_size + (stack_size - index))
                    elif j*vel+i+vel+1 <= ((self.board_size * self.board_size) // 2):
                        dd_size = 9 - info[2][j*vel+i+vel+1].count(".") #velicina steka dole desno
                        if dd_size > 0:
                            if info[2][j*vel+i][stack_size-1] == "O":
                                for index in o_stack_position:
                                    if dd_size + (stack_size - index) == 8:
                                        return 10
                                    elif dd_size + (stack_size - index) < 8:
                                        if dd_size + (stack_size - index) > value:
                                            value = dd_size + (stack_size - index)
                            else:
                                for index in o_stack_position:
                                    if dd_size + (stack_size - index) == 8:
                                        value = -10
                                    elif dd_size + (stack_size - index) < 8:
                                        if -(dd_size + (stack_size - index)) > value:
                                            value = -(dd_size + (stack_size - index))
        if value == 0:
            value = 1
        return value
                
    def computer_make_move(self, move, player, info, final_move = False):
        letter = move[0][0].upper()
        number = int(move[0][1:])
        letNum = (ord(letter) - 65) // 2 
        numNum = number // 2 
        if((ord(letter) - 65)% 2 ==1):
            numNum+= self.board.num_of_fields//2-1
        
        table_copy=info[2][:]
        row = letNum*self.board.num_of_fields + numNum
        a = table_copy[row]

        removed_elements = a[int(move[1]):]
        a[int(move[1]):] = ["."] * len(removed_elements)
        
        if move[2]=="DL":
            if((ord(letter) - 65)% 2 ==1):
                letNum+=1
            
            number-=1
            pom = (ord(letter) - 65)+1
            
        elif move[2] == "DD":
            if((ord(letter) - 65)% 2 ==1):
                letNum+=1
            
            number+=1
            pom = (ord(letter) - 65)+1

        elif move[2] == "GL":
            if((ord(letter) - 65)% 2 ==0):
                letNum-=1
            
            number-=1
            pom = (ord(letter) - 65)-1

        elif move[2] == "GD":
            if((ord(letter) - 65)% 2 ==0):
                letNum-=1
            
            number+=1
            pom = (ord(letter) - 65)-1

        numNum = number // 2 
        if(pom % 2 ==1):
            numNum+= self.board.num_of_fields//2-1
        rowrow=letNum*self.board.num_of_fields+numNum

        a_new=table_copy[rowrow]
        non_empty_elements = [element for element in removed_elements if element != "."]
        for element in non_empty_elements:
            first_dot_index = a_new.index('.')
            a_new.insert(first_dot_index, element)

        player1 = 0
        player2 = 0
        
        non_empty=[element for element in a_new if element !="."]
        if len(non_empty)==8:
            last_element_color = non_empty[-1]
            
            #if last_element_color == self.current_player.checker_color.value:
            #print("last element: ", last_element_color)
            #print("player: ", player)
            if last_element_color == player:
                #print("jeste")
                if player == "X":
                    player1 += 1
                elif player == "O":
                    player2 += 1
                if final_move:
                    self.current_player.stacks += 1
                    print(f"Number of {self.current_player.checker_color.value}'s stacks: {self.current_player.stacks} ")
                    print(self.current_player.stacks)

                for i in range(8):
                    a_new[i] = '.'
        new_info = (info[0]+player2, info[1]+player1, table_copy)
        #self.board.drawTable(new_info[2])
        #print(new_info[0], ", ", new_info[1])
        return new_info

    def make_move(self):
        possible_moves=self.player_possible_moves(self.current_player.checker_color.value)#ne valja treba da se filtriraju potezi
            
        print(possible_moves)
        load_input = True
        move = True
        while move:
            while load_input:
                move_input = input(f"{self.current_player.checker_color.value}'s turn. Enter your move (position stack_place direction): ")
                move_parts = move_input.split()
                
                if len(move_parts) != 3:
                    print("Invalid input. Please enter position, stack place, and direction.")
                    #continue
                else:
                    load_input = False
            
            position, stack_place, direction = move_parts
                
            #print(self.possible_next_moves(position))
                
            #print(self.get_stack_position('B2', 'X'))
        
            move_found = False
            for moves_list in possible_moves:
                for move_tuple in moves_list:
                    if move_tuple == (position, int(stack_place), direction):
                        move_found = True
                        break

            if move_found:
                print("Valid move.")
                move=False
                self.update_board(position, stack_place, direction)
                if self.is_game_over():
                    print(f"Congrats {self.current_player.checker_color.value}! You won the game")
                else:
                    self.board.drawTable()
            else:
                print("Invalid move. Please enter a valid move.")
                load_input=True
        
            
    
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
    
    def update_board(self, position, stack_place, direction):
        letter = position[0].upper()
        number = int(position[1:])
        letNum = (ord(letter) - 65) // 2 
        numNum = number // 2 
        if((ord(letter) - 65)% 2 ==1):
            numNum+= self.board.num_of_fields//2-1
            
        row = letNum*self.board.num_of_fields + numNum
        a = self.board.fields[row]

        removed_elements = a[int(stack_place):]
        a[int(stack_place):] = ["."] * len(removed_elements)
            
        
        if direction=="DL":
            if((ord(letter) - 65)% 2 ==1):
                letNum+=1
            
            number-=1
            pom = (ord(letter) - 65)+1
            
        elif direction == "DD":
            if((ord(letter) - 65)% 2 ==1):
                letNum+=1
            
            number+=1
            pom = (ord(letter) - 65)+1

        elif direction == "GL":
            if((ord(letter) - 65)% 2 ==0):
                letNum-=1
            
            number-=1
            pom = (ord(letter) - 65)-1

        elif direction == "GD":
            if((ord(letter) - 65)% 2 ==0):
                letNum-=1
            
            number+=1
            pom = (ord(letter) - 65)-1

        numNum = number // 2 
        if(pom % 2 ==1):
            numNum+= self.board.num_of_fields//2-1
        rowrow=letNum*self.board.num_of_fields+numNum

        a_new=self.board.fields[rowrow]
        non_empty_elements = [element for element in removed_elements if element != "."]
        for element in non_empty_elements:
            first_dot_index = a_new.index('.')
            a_new.insert(first_dot_index, element)

        
        non_empty=[element for element in a_new if element !="."]
        if len(non_empty)==8:
            last_element_color = non_empty[-1]
            
            if last_element_color == self.current_player.checker_color.value:
                self.current_player.stacks += 1
                print(f"Number of {self.current_player.checker_color.value}'s stacks: {self.current_player.stacks} ")
                print(self.current_player.stacks)

                for i in range(8):
                    a_new[i] = '.'

    def is_game_over(self):
        return self.current_player.stacks > self.max_num_of_stacks // 2

    def player_possible_moves(self, player, table=None):
        board = self.board.fields if table is None else table
        moves = []
        for pom in range(0, 32):
            if player in board[pom]:
                let = pom // 4 + 65
                position = chr(let)
                p = pom // 4
                if p % 2 == 0:
                    number = (pom * 2) % self.board_size + 1
                    position += str(number)
                else:
                    number = (pom * 2 + 1) % self.board_size + 1
                    position += str(number)
                moves.append(self.possible_next_moves(position, player, board))
        return moves

    def possible_next_moves(self, position, player, table = None):
        board = self.board.fields if table is None else table
        visited = set()
        queue = deque([(position, 0, [])])
        closest_neighbors = []

        min_length=self.board_size

        while queue:
            current_node, distance, route = queue.popleft()

            if self.check_position(current_node, board) and min_length >= distance and distance != 0:
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
            for pomm in self.get_stack_position(position, player, board):
                if (position, pomm, move) not in possible_moves:
                        rows = self.get_rows_by_position(position, move, board)
                        # print((position, pomm, move), rows)
                        a = rows[0].index('.') - pomm
                        b = rows[1].index('.')
                        # print(a,pomm,b)
                        if a + b <= 8 and pomm < b:
                            possible_moves.append((position, pomm, move))
        return possible_moves
    
    # def check_if_next_move_valid(self, position, pomm, move):
        # flag = True
        # column = int(position[1:])
        # current_field = get_row_by_position(position)
        # next_position = 0
        # if move[0] == 'G':
            # if column % 2 == 0:
                # next_position
    
    # def get_row_by_position(self,position):
        # letter = position[0].upper()
        # number = int(position[1:])
        # letNum = (ord(letter) - 65) // 2 
        # numNum = number // 2 
        # if((ord(letter) - 65)% 2 ==1):
            # numNum+= self.board.num_of_fields//2-1
            
        # row = letNum*self.board.num_of_fields + numNum
        # return self.board.fields[row]
        
    def get_rows_by_position(self,position, move, table = None):
        board = self.board.fields if table is None else table
        letter = position[0].upper()
        number = int(position[1:])
        letNum = (ord(letter) - 65) // 2 
        numNum = number // 2 
        if((ord(letter) - 65)% 2 ==1):
            numNum+= self.board.num_of_fields//2-1
                        
        row = letNum*self.board.num_of_fields + numNum
                
        nextRow = row
        if((ord(letter) - 65)% 2 ==1):
            if move[0] == 'G':
                nextRow-=4
            else:
                nextRow+=4
        else:
            if move[0] == 'G':
                nextRow-=5
            else:
                nextRow+=3
        if move[1] == 'D':
                nextRow+=1
                
        a = board[row]
        b = board[nextRow]
        c = []
        c.append(a)
        c.append(b)
        return c
        
    # def check_if_neighbors_empty(self, node):
        # for neighbor in self.board.table_graph[node]:
            # neighbor_row = get_row_by_position(neighbor)
            # if neighbor_row.index('.') > 0:
                # return False
        # return True

    def check_position(self, position, table = None):
        board = self.board.fields if table is None else table
        letter = position[0].upper()
        number = int(position[1:])
        letNum = (ord(letter) - 65) // 2 
        numNum = number // 2 
        if((ord(letter) - 65)% 2 ==1):
            numNum+= self.board.num_of_fields//2-1
                
        row = letNum*self.board.num_of_fields + numNum
        if('X' in board[row] or 'O' in board[row]):
            return True
        return False

    def get_stack_position(self, position, player, table = None):
        board = self.board.fields if table is None else table
        letter = position[0].upper()
        number = int(position[1:])
        letNum = (ord(letter) - 65) // 2 
        numNum = number // 2 
        if((ord(letter) - 65)% 2 ==1):
            numNum+= self.board.num_of_fields//2-1
                
        row = letNum*self.board.num_of_fields + numNum
        positions = [index for index in range(0, 8) if board[row][index] == player]
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

