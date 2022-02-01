# Author: Esteban Cajamarca GitHub username: EstebanCajamarca Date: 1/31/2022 Write a class named Taxicab that has
# three private data members: one that holds the current x-coordinate, one that holds the current y-coordinate,
# and one that holds the current odometer reading (the actual odometer distance driven by the Taxicab,
# not the Euclidean distance from its starting point). All three data members should be updated as needed so that
# they are always current.
#
# The class should have an init method that takes two parameters and uses them to initialize the coordinates,
# and also initializes the odometer to zero.
#
# The class should have get methods for each data member: get_x_coord, get_y_coord, and get_odometer. The class does
# not need any set methods.
#
# It should have a method called move_x that takes a parameter that tells how far the Taxicab should shift left or
# right. It should have a method called move_y that takes a parameter that tells how far the Taxicab should shift up
# or down.


class Taxicab:
    """Gives odometer reading of Taxicab depending on coordinates movement."""

    def __init__(self, x_coord, y_coord, odometer=0):
        """Defines initial values for x, y and odometer variables."""
        self._x_coord = x_coord
        self._y_coord = y_coord
        # odometer should start in zero.
        self._odometer = 0

    def get_x_coord(self):
        """Obtains new values for x coordinates."""
        return self._x_coord

    def get_y_coord(self):
        """Obtains new values for y coordinates."""
        return self._y_coord

    def move_x(self, x_move):
        """Adds x movement to odometer reading"""
        self._odometer += abs(x_move)  # takes absolute value of x_move
        self._x_coord += x_move  # updating coordinates in x

    def move_y(self, y_move):
        """Adds y movement to odometer reading."""
        self._odometer += abs(y_move)  # takes absolute value of y_move
        self._y_coord += y_move  # updating coordinates in y

    def get_odometer(self):
        """Calculates odometer reading depending on entered values for coordinates x and y."""
        return self._odometer


"""testing
cab = Taxicab(5, -8)  # creates a Taxicab object at coordinates (5, -8)
cab.move_x(3)
cab.move_x(-1)
cab.move_y(-4)
print(cab.get_odometer())
print(cab.get_y_coord())
print(cab.get_x_coord())"""
