# Author: Matthew Yang
# Date: 11/30/2019
# Description: Create a class named FBoard which can track a game, give its
#              current state and determine if there is a winner.

class FBoard:
    """
    Class representing a game of x's versus o's which can analyze moves and
    determine if and when there is a winner based on the rules provided.
    """
    
    def __init__(self):
        """
        Initializes the board, game state and starting positions for the game
        pieces.
        """
        self._board = [
            ["-", "-", "-", "x", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["o", "-", "o", "-", "o", "-", "o", "-"],
        ]
        self._game_state = "UNFINISHED"
        self._x_row = 0
        self._x_column = 3
        
    def get_game_state(self):
        """
        Returns the given state of the game.
        """
        return self._game_state
        
    def move_x(self, row, column):
        """
        Determines if the move can be made for x as well as determines if the
        move results in x winning the game.
        """
        # Return false if the game is over or if the requested move is not valid
        if (self._game_state != "UNFINISHED") or not self.valid_x_move(row, column):
            return False
            
        # Reset the previous x coordinate and change destination to an x
        self._board[self._x_row][self._x_column] = "-"
        self._board[row][column] = "x"
            
        # Set the new x coordinates to corresponding data members
        self._x_row = row
        self._x_column = column
            
        # Determine if x won the game and update state if so
        if row == 7:
            self._game_state = "X_WON"
        
        return True
        
    def move_o(self, from_row, from_column, to_row, to_column):
        """
        Determines if the move can be made for o as well as determines if the
        move results in o winning the game.
        """
        # Return false if the game is over or if the requested move is not valid
        if (self._game_state != "UNFINISHED") or not self.valid_o_move(from_row, from_column, to_row, to_column):
            return False
        
        # Reset the previous o coordinate and change destination to an o
        self._board[from_row][from_column] = "-"
        self._board[to_row][to_column] = "o"
        
        # Determine if o won the game and update state if so
        if not self.any_remaining_x_moves():
            self._game_state = "O_WON"
            
        return True
        
    def valid_x_move(self, row, column):
        """
        Determines if the requested move is valid based on the current position
        of the x.
        """
        # Determine if the requested move meets the requirements to be valid
        if self.in_bounds(row) and self.in_bounds(column) and self._board[row][column] == "-":
            if (column == self._x_column - 1) or (column == self._x_column + 1):
                return (row == self._x_row - 1) or (row == self._x_row + 1)
            
        return False
        
    def valid_o_move(self, from_row, from_column, to_row, to_column):
        """
        Determines if the requested move is valid for o based on the to and from 
        coordinates given.
        """
        # Determine if the requested move meets the requirements to be valid
        if self.in_bounds(to_row) and self.in_bounds(to_column):
            if (self._board[from_row][from_column] == "o") and (self._board[to_row][to_column] == "-"):
                if (to_column == from_column - 1) or (to_column == from_column + 1):
                    return to_row == from_row - 1
            
        return False
        
    def in_bounds(self, value):
        """
        Helper method to determine if a value is within the limits of the board.
        """
        return value in range(0, 8)
        
    def any_remaining_x_moves(self):
        """
        Determine if there are any remaining valid moves for x based on it's
        current position.
        """
        # List of tuples containing the four different directions x can move
        surrounding_coordinates = [
            (self._x_row - 1, self._x_column + 1),
            (self._x_row - 1, self._x_column - 1),
            (self._x_row + 1, self._x_column + 1),
            (self._x_row + 1, self._x_column - 1),
        ]
        
        # Iterate the surrounding coordinates and return true if a valid one is
        # found
        for coordinate in surrounding_coordinates:
            if self.valid_x_move(coordinate[0], coordinate[1]):
                return True
                
        return False

    def print_board(self):
        """
        Prints the game board in 8 rows of 8.
        """
        # Iterate the rows and build a string representation to print
        for row in self._board:
            row_string = ""
            
            for value in row:
                row_string += value + " "
                
            print(row_string)
