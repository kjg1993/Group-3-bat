from game.point import Point
from game import constants
class Actor:

    def __init__(self):
        self._text = ""
        self._position = Point(0,0)
        self._velocity = Point(0,0)
        

    def set_position(self, position):
        """sets the acotrs position in 2d space
        """
        self._position = position

    def set_text(self, text):
        """sets the acotrs text.
        """

        self._text = text

    def set_velocity(self, velocity):
        """sets the acotrs velocity
        """

        self._velocity = velocity

    def get_position(self):

        return self._position

    def get_velocity(self):
        return self._velocity

    def get_text(self):

        return self._text
