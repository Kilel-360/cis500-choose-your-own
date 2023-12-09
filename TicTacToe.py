
#######################################################
# TicTacToe
#
# Name: Kilel Chepngeno Joyce

# Section: 02
#
# Fall 2023
#########################################################
# Works Cited

"""
1. "Algorithm for Determining Tic Tac Toe Game Over." Stack Overflow,
         stackoverflow.com/questions/1056316/algorithm-for-determining-tic-tac-toe-game-over. Accessed 9 Dec. 2023.

2. "Implementation of Tic-Tac-Toe Game." GeeksforGeeks, 20 Feb. 2023, 
www.geeksforgeeks.org/implementation-of-tic-tac-toe-game/. Accessed 8 Dec. 2023.

3. Python, Real. "Build a Tic-Tac-Toe Game With Python and Tkinter." 
Python Tutorials – Real Python, 27 June 2022, realpython.com/tic-tac-toe-python/. Accessed 8 Dec. 2023.
"""
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if not self.game_over and 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.check_winner(row, col)
            self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        if all(self.board[row][i] == self.current_player for i in range(3)):
            self.winner = self.current_player
            self.game_over = True

            # Checking column
        if all(self.board[i][col] == self.current_player for i in range(3)):
            self.winner = self.current_player
            self.game_over = True

            # Checking diagonals
        if row == col or row + col == 2:
            if all(self.board[i][i] == self.current_player for i in range(3)) or \
                    all(self.board[i][2 - i] == self.current_player for i in range(3)):
                self.winner = self.current_player
                self.game_over = True

            # Checking for a tie
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)) and not self.game_over:
            self.game_over = True
            self.winner = None

    def check_tie(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3)) and not self.game_over

    def is_game_over(self):
        return self.game_over

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False

    def validate_input(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def display_current_player(self):
        print(f"Current player: {self.current_player}")

    def valid_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def is_valid_move(self, row, col):
        return (row, col) in self.valid_moves()

    def is_tie(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3)) and not self.game_over

    def display_winner(self):
        if self.winner:
            print(f"The winner is: {self.winner}")
        elif self.is_tie():
            print("The game is tied!")

