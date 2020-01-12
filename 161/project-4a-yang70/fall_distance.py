# Author: Matthew Yang
# Date: 10/15/2019
# Description: Function that takes the falling time as an argument and returns the distance in meters the
#              object has fallen in that time.

def fall_distance(time):
    """Returns the distance in meters an object would fall given the input time."""
    return 0.5 * 9.8 * (time**2)
