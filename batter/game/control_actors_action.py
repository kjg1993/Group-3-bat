from game import constants
from game.action import Action
class ControlActorsAction:
    
    def __init__(self, input):
        self._input_service = input

    def execute(self, cast):


        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0]
        paddle.set_velocity(direction)
