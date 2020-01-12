# Author: Matthew Yang
# Date: 10/23/2019
# Description: Taxicab class.  Init takes initial x/y coordinates and
#              initializes an odometer to zero.  The class also has instance
#              methods for moving x and moving y, which updates the odometer.
#              Finally the class has getter methods for all data members.

class Taxicab:
    """
    Represents a taxi cab with starting coordinates and methods to move, get
    distance traveled as well as return current coordinates
    """

    def __init__(self, x, y):
        """
        Initialize x and y coordinates and the odometer to zero
        """
        self._x = x
        self._y = y
        self._odometer = 0
    
    def get_x_coord(self):
        """
        Getter for x coordinate
        """
        return self._x
        
    def get_y_coord(self):
        """
        Getter for y coordinate
        """
        return self._y

    def get_odometer(self):
        """
        Getter for odometer
        """
        return self._odometer

    def move_x(self, distance):
        """
        Moves the x coordinate the given distance
        """
        self._x += distance
        self._update_odometer(distance)
        
    def move_y(self, distance):
        """
        Moves the y coordinate the given distance
        """
        self._y += distance
        self._update_odometer(distance)
        
    def _update_odometer(self, distance):
        """
        Private method for updating the odometer with the distance traveled
        """
        if distance < 0:
            self._odometer += distance * -1
        else:
            self._odometer += distance
