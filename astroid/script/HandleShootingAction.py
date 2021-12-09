import time

from genie.script.action import InputAction
from genie.services import keys

from astroid.cast.bullet import Bullet

# BULLET_VX = 0
# BULLET_VY = -10
ATTACK_INTERVAL = 0.25   # seconds

class HandleShootingAction(InputAction):
    def __init__(self, priority, keyboard_service, audio_service):
        super().__init__(priority)
        self._ship = None
        self._ship_2 = None
        self._ship_3 = None
        self._ship_4 = None
        self._last_bullet_spawn = time.time()  # seconds
        self._last_bullet_dict = {"ship": self._last_bullet_spawn, "ship_2": self._last_bullet_spawn, "ship_3": self._last_bullet_spawn, "ship_4": self._last_bullet_spawn}
        self._keyboard_service = keyboard_service
        self._audio_service = audio_service
    
    def _spawn_bullet(self, clock, actors, bullet_vx, bullet_vy, ship, rotation, name):
        """
            Only spawn a bullet if:
                - The time from the last time bullet spawn until now is >= ATTACK_INTERVAL
                - The ship is still alive (not None)
        """
        time_since_last_shot = time.time() - self._last_bullet_dict[name]     #Measured in seconds
        if ship != None and time_since_last_shot >= ATTACK_INTERVAL:
            # Bullet's starting position should be right on top of the ship
            bullet_x = ship.get_x()
            bullet_y = ship.get_y() - (ship.get_height() / 2)

            if name == "ship":
                bullet_y -= 10
            if name == "ship_2":
                bullet_y += 80
            if name == "ship_3":
                bullet_x -= 50
                bullet_y += 20
            if name == "ship_4":
                bullet_x += 50
                bullet_y += 20
            
            # Spawn bullet
            bullet = Bullet("astroid/assets/bullet.png", 20, 30, x = bullet_x, y = bullet_y, vx = bullet_vx, vy = bullet_vy)
            actors.add_actor("bullets", bullet)

            # Rotate the bullet to which player shot
            bullet.set_rotation(rotation)

            # Play the shooting sound :)
            self._audio_service.play_sound("astroid/assets/sound/bullet_shot.wav", 0.1)

            # Record the time this bullet spawns
            self._last_bullet_spawn = time.time()
            self._last_bullet_dict[name] = self._last_bullet_spawn

    def execute(self, actors, actions, clock, callback):
        """
            Handle the shooting when the user presses SPACE
        """
        # Look for the ship first to make sure it's still alive
        self._ship = actors.get_first_actor("ship")
        
        # If Space is pressed, spawn a bullet
        if (self._keyboard_service.is_key_down(keys.UP) or self._keyboard_service.is_key_down(keys.DOWN)) and self._ship != None:
            self._spawn_bullet(clock, actors, 0, -10, self._ship, self._ship.get_rotation(), "ship")

        self._ship_2 = actors.get_first_actor("ship_2")
        if (self._keyboard_service.is_key_down(keys.S) or self._keyboard_service.is_key_down(keys.W)) and self._ship_2 != None:
            self._spawn_bullet(clock, actors, 0, 10, self._ship_2, self._ship_2.get_rotation(), "ship_2")

        self._ship_3 = actors.get_first_actor("ship_3")
        if (self._keyboard_service.is_key_down(keys.J) or self._keyboard_service.is_key_down(keys.L)) and self._ship_3 != None:
            self._spawn_bullet(clock, actors, -10, 0, self._ship_3, self._ship_3.get_rotation(), "ship_3")

        self._ship_4 = actors.get_first_actor("ship_4")

        if (self._keyboard_service.is_key_down(keys.KP4) or self._keyboard_service.is_key_down(keys.KP6)) and self._ship_4 != None:
            self._spawn_bullet(clock, actors, 10, 0, self._ship_4, self._ship_4.get_rotation(), "ship_4")