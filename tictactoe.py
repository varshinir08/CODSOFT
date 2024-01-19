import math

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.human_player = 'X'
        self.ai_player = 'O'
        self.current_player = self.human_player

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i * 3 + j] == player for j in range(3)) or \
               all(self.board[i + j * 3] == player for j in range(3)):
                return True
        if all(self.board[i] == player for i in [0, 4, 8]) or \
           all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner(self.human_player) or \
               self.is_winner(self.ai_player) or \
               self.is_full()

    def get_empty_cells(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.switch_player()
            return True
        else:
            print("Invalid move. Cell already occupied.")
            return False

    def switch_player(self):
        self.current_player = self.human_player if self.current_player == self.ai_player else self.ai_player

    def minimax(self, depth, alpha, beta, maximizing_player):
        if self.is_winner(self.human_player):
            return -1
        if self.is_winner(self.ai_player):
            return 1
        if self.is_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_empty_cells():
                self.make_move(move)
                eval = self.minimax(depth + 1, alpha, beta, False)
                self.board[move] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_empty_cells():
                self.make_move(move)
                eval = self.minimax(depth + 1, alpha, beta, True)
                self.board[move] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(self):
        best_val = float('-inf')
        best_move = -1
        alpha = float('-inf')
        beta = float('inf')

        for move in self.get_empty_cells():
            self.make_move(move)
            move_val = self.minimax(0, alpha, beta, False)
            self.board[move] = ' '

            if move_val > best_val:
                best_move = move
                best_val = move_val

            alpha = max(alpha, move_val)

        return best_move

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("You are 'X', and the AI is 'O'.")
        print("The board positions are numbered from 1 to 9.")

        while not self.is_game_over():
            self.print_board()

            if self.current_player == self.human_player:
                position = self.get_human_move()
            else:
                print("AI is making a move...")
                position = self.find_best_move()

            self.make_move(position)

        self.print_board()

        if self.is_winner(self.human_player):
            print("Congratulations! You win!")
        elif self.is_winner(self.ai_player):
            print("AI wins! Better luck next time.")
        else:
            print("It's a draw! Good game!")

    def get_human_move(self):
        while True:
            try:
                position = int(input("Enter your move (1-9): ")) - 1
                if position in range(9) and self.board[position] == ' ':
                    return position
                else:
                    print("Invalid move. Please choose an empty cell.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

