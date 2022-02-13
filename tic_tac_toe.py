"""
A Tic-TAC-TOE game made with OOP
Code regarding printing the board and taking position inputs was inspired from an UDEMY Course
Course link: 'https://www.udemy.com/course/complete-python-bootcamp/'
"""
class Board():

    def __init__(self):
        self.board = [" "]*10
        self.player_one = []
        self.player_two = []

    def place_marker(self,position,marker):
        if self.board[position] == " ":
            self.board[position] = marker
        else:
            print("\nChoose another position")
    
    def print_board(self):
        print()
        print("-------------")
        print(self.board[7] + "  |  " + self.board[8] + "  |  " + self.board[9])
        print("-------------")
        print(self.board[4] + "  |  " + self.board[5] + "  |  " + self.board[6])
        print("-------------")
        print(self.board[1] + "  |  " + self.board[2] + "  |  " + self.board[3])
        print("-------------")
    
    def inputs(self):
        self.player_one.append(input("Player one enter your name: "))
        self.player_two.append(input("Player two enter your name: "))

        while True:
            marker_choice = input("Player one choose your marker: ")
            if marker_choice not in "XO":
                print("Enter a valid marker")
                continue
            else:
                self.player_one.append(marker_choice)
                if marker_choice == "X":
                    self.player_two.append("O")
                else:
                    self.player_two.append("X")
                    break
    
    def position_inputs(self):
        while True:
            try:
                position = int(input('Enter your position (1-9): '))
                return position
            except:
                print("Enter a number between 1 to 9 (inclusive)") 

    def win_check(self,player):
        if self.board[9] == self.board[8] == self.board[7] == player[1]:
            print(player[0] + " has won the game")
            return True
        elif self.board[4] == self.board[5] == self.board[6] == player[1]:
            print(player[0] + " has won the game")
            return True
        elif self.board[1] == self.board[2] == self.board[3] == player[1]:
            print(player[0] + " has won the game")
            return True
        elif self.board[9] == self.board[5] == self.board[1] == player[1]:
            print(player[0] + " has won the game")
            return True
        elif self.board[7] == self.board[5] == self.board[3] == player[1]:
            print(player[0] + " has won the game")
            return True
        elif self.board[1] == self.board[4] == self.board[7] == player[1]:
            print(player[0] + " has won the game")
            return True
        elif self.board[2] == self.board[8] == self.board[5] == player[1]:
            print(player[0] + " has won the game")
            return True
        elif self.board[3] == self.board[6] == self.board[9] == player[1]:
            print(player[0] + " has won the game")
            return True
        else:
            return False

    def play_again(self):
        while True:
            choice = input("Do you want to play again (yes or no): ")
            if choice not in "yesno":
                print("Enter a valid response")
                continue
            else:
                if choice == 'yes':
                    return True
                else:
                    return False

    def run(self):

        print("Welcome to TIC-TAC-TOE game")
        self.inputs()
        self.print_board()
        play = True
        
        while play:
            
            print("Player one place your mark")
            position = self.position_inputs()
            self.place_marker(position,self.player_one[1])
            self.print_board()
            if self.win_check(self.player_one):
                play = self.play_again()
                continue

            print("Player two place your mark")
            position = self.position_inputs()
            self.place_marker(position,self.player_two[1])
            self.print_board()
            if self.win_check(self.player_two):
                play = self.play_again()
                continue

       
new_game = Board()
new_game.run()
        
# Contact 
# sp357@njit.edu