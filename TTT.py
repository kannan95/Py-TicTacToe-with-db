from dashboard import *


class tictactoe:
    def __init__(self, board):
        self.board = board

    def display_board(self):
        # To Print the Board of TicTacToe
        print("=" * 10)
        print(self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('~' * 9)
        print(self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('~' * 9)
        print(self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        print("=" * 10)


    def win_check(self, player):
        # To check rows
        if (self.board[0] == self.board[1] == self.board[2] != " ") or (
                    self.board[3] == self.board[4] == self.board[5] != " ") or (
                    self.board[6] == self.board[7] == self.board[8] != " "):
            self.winner(True, player)
        # To check columns
        elif ((self.board[0] == self.board[3] == self.board[6] != " ") or (
                    self.board[1] == self.board[4] == self.board[7] != " ") or (
                    self.board[2] == self.board[5] == self.board[8] != " ")):
            self.winner(True, player)
        # To check diagonals
        elif ((self.board[0] == self.board[4] == self.board[8] != " ") or (
                    self.board[2] == self.board[4] == self.board[6] != " ")):
            self.winner(True, player)
        else:
            # Checking Draw
            count = True
            for i in range(9):
                if self.board[i] == " ":
                    count = False
            if count:
                self.winner(False, None)

    def winner(self, check, player_name):
        global player1_values
        global player2_values

        # checks the winner
        if check:
            print(">>> {} wins <<<".format(player_name))
            if (player_name == player1):
                player1_values[0], player1_values[1] = 1, 0
                player2_values[1], player2_values[0] = 1, 0
            else:
                player2_values[0], player2_values[1] = 1, 0
                player1_values[1], player1_values[0] = 1, 0
        elif check is False:
            print(">>> Its draw <<<")
            player1_values[2] = 1
            player2_values[2] = 1
        import sql
        sql.sql_main()


    def input_check(self, player_name):
        while True:
            try:
                number = int(input(player_name + "\'s move >>>"))
                if not (1 <= number < 10):
                    print("Wrong input. Please input between 1 and 9!")
                elif (self.board[number - 1] == 'X' or self.board[number - 1] == 'O'):
                    print("Wrong input. Its already stroked!")
                else:
                    return number
            except:
                print("Please, Give proper input!")


def ttt_main():
    board = [' '] * 9
    obj = tictactoe(board)

    while True:
        User1_input = obj.input_check(player1)
        board[User1_input - 1] = 'X'
        obj.display_board()
        obj.win_check(player1)

        User2_input = obj.input_check(player2)
        board[User2_input - 1] = 'O'
        obj.display_board()
        obj.win_check(player2)


player1_values = [0, 0, 0]
player2_values = [0, 0, 0]

if __name__ == "__main__":
    ttt_main()
