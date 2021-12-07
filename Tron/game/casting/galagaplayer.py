import constants
from game.casting.actor import Actor
from game.shared.point import Point


class GalagaPlayer(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self.player = None
    
    def prepare_player(self, position, velocity, color):
        player = Actor()
        player.set_position(position)
        player.set_velocity(velocity)
        player.set_text("#")
        player.set_color(color)