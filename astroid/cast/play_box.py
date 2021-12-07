from genie.cast.actor import Actor

class play_box(Actor):
    def __init__(self, path: str, width: int, height: int, x: float = 0, y: float = 0, vx: float = 0, vy: float = 0, rotation: float = 0, rotation_vel: float = 0, flipped: bool = False):
        super().__init__(path, width, height, x=x, y=y, vx=vx, vy=vy, rotation=rotation, rotation_vel=rotation_vel, flipped=flipped)