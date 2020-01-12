# Author: Matthew Yang
# Date: 11/21/2019
# Description: Create a class named TicTacToe which can track a game, give its
#              current state and determine if there is a winner or if it was a
#              draw.

class TicTacToe:
    """
    Class that represents a Tic Tac Toe game which can analyze it's given board
    and determine when a game is complete and if there was a winner or draw.
    """

    def __init__(self):
        """
        Initialize the board of a list containing 3 other lists of empty
        strings representing the game rows.
        """
        self._board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self._current_state = "UNFINISHED"
        self._move_counter = 0

    def get_current_state(self):
        """
        Returns the current state of the game.
        """
        return self._current_state

    def make_move(self, row, column, symbol):
        """
        Takes row, column and symbol arguments and attempts to apply them to the
        current board. Returns false if the given move is not possible or if the
        state of the game is not unfinished.
        """
        # Return false unless the game is unfinished and the move is allowed
        if (self._current_state != "UNFINISHED") or not self.available(row, column) or not self.valid_symbol(symbol):
            return False

        self._board[row][column] = symbol
        self._move_counter += 1
        winner = self.find_winner(row, column, symbol)

        # Set the current state to the winner if there is one, otherwise check
        # if there are any more moves available and if not set current state to
        # draw.
        if winner:
            self._current_state = symbol.upper() + "_WON"
        elif self._move_counter == 9:
            self._current_state = "DRAW"

        return True

    def available(self, row, column):
        """
        Helper method to check if the given space is available. Returns True or
        False.
        """
        if row > 2 or row < 0 or column > 2 or column< 0:
            return False

        return self._board[row][column] == ""

    def valid_symbol(self, symbol):
        """
        Helper method to check if the given symbol is an x or o. Returns True or
        False.
        """
        return symbol == "x" or symbol == "o"

    def find_winner(self, row, column, symbol):
        """
        Takes the row, column and symbol of the last move and checks if that
        symbol has won.
        """
        # If the move count is less than 3 there can be no winner yet
        if self._move_counter < 3:
            return False

        # Helper to determine if last move was a corner
        corners = [
            [0, 0],
            [0, 2],
            [2, 0],
            [2, 2]
        ]

        # Check the row
        if self._board[row] == [symbol, symbol, symbol]:
            return symbol
        # Check the column
        elif self._board[0][column] == symbol and self._board[1][column] == symbol and self._board[2][column] == symbol:
            return symbol
        # If the center matches the symbol and the last move was a corner, check the diagonals
        elif self._board[1][1] == symbol and [row, column] in corners:
            if self._board[0][0] == symbol and self._board[2][2] == symbol:
                return symbol
            elif self._board[0][2] == symbol and self._board[2][0] == symbol:
                return symbol

        # Explicitly return false if a winning sequence was not found
        return False

    def print_board(self):
        """
        Prints the game board in 3 rows of three, replacing empty spots with
        dashes.
        """
        for row in self._board:
            print(
                "-" if row[0] == "" else row[0],
                "-" if row[1] == "" else row[1],
                "-" if row[2] == "" else row[2],
            )
