from genie.script.action import UpdateAction
from astroid.cast.astroid import Astroid

import random
import time

SPAWN_INTERVAL = 1.5          # seconds
LARGE_SIZE = (40, 55)

LARGE = 1
MEDIUM = 2
SMALL = 3

class SpawnEnemiesAction(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._timer_started = False
        self._last_spawn = 0 # seconds
        self._window_size = window_size
        self._enemy_spawn = False

    def _create_enemy(self, x: int, y:int):
        """
            This is a helper function that creates an astroid based on
            the input "type" and the initial position
        """
        vel_x = -1 if x > self._window_size[0] / 2 else 1
        vel_y = 3
        return Astroid("astroid/assets/astroids/galaga_enemy.png",
                        health_bar_y_offset=LARGE_SIZE[1]/2+5,
                        health_bar_height=5,
                        width = LARGE_SIZE[0],
                        height = LARGE_SIZE[1],
                        x = x, y = y,
                        vx = vel_x, vy = vel_y,
                        rotation_vel=1,
                        points=5, max_hp=2, show_text_health=True)

    def execute(self, actors, actions, clock, callback):
        """
            - Check to see if it's time to spawn another astroid
            - Randomly pick Small, Medium, or Large
            - Pick and initial position for the astroid
            - Create the astroid by calling self._create_astroid_by_type
            - Add the astroid to the cast
            - Record the most recent spawn
        """
        if not self._timer_started:
            self._timer_started = True
            self._last_spawn = time.time()
        
        if time.time() - self._last_spawn >= SPAWN_INTERVAL:
            # Pick a random type of astroid: Small, Medium, Large
            astroid_type = random.randint(1,3)

            # Generate a random position on top of the screen,
            #  limit the spawn range from 1/8 of the screen to 7/8 of the screen
            lower_x_bound = int(self._window_size[0] / 8)
            upper_x_bound = int(self._window_size[0] - lower_x_bound)

            start_pos_x = random.randint(lower_x_bound, upper_x_bound) 
            start_pos_y = 0

            # spawn an astroid
            astroid = self._create_enemy(start_pos_x, start_pos_y)
            actors.add_actor("astroids", astroid)

            # set last_spawn to current frame
            self._last_spawn = time.time()