from genie.script.action import InputAction
from genie.services import keys

VEL = 4

class HandleShipMovementAction(InputAction):
    def __init__(self, priority, keyboard_service):
        super().__init__(priority)
        self._keyboard_service = keyboard_service
        self._ship = None
        self._ship_2 = None
        self._ship_3 = None
        self._ship_4 = None

    def execute(self, actors, actions, clock, callback):
        """
            This action handles the input of the player to make the ship move
        """
        # Look for the ship among the actors if we haven't already known it
        self._ship = actors.get_first_actor("ship")
        
        # Don't worry about it if ship doesn't exist
        if (self._ship != None):
            # Check which keys are pressed and update the ship's velocity accordingly
            keys_state = self._keyboard_service.get_keys_state(keys.LEFT, keys.RIGHT, keys.DOWN, keys.UP)
            if keys_state[keys.LEFT]:
                self._ship.set_vx(-VEL)
            if keys_state[keys.RIGHT]:
                self._ship.set_vx(VEL)
            # if keys_state[keys.DOWN]:
            #     self._ship.set_vy(VEL)
            # if keys_state[keys.UP]:
            #     self._ship.set_vy(-VEL)
            
            # If keys in either dirrection are not pressed, set velocity of that direction to 0
            if not keys_state[keys.LEFT] and not keys_state[keys.RIGHT]:
                self._ship.set_vx(0)
            if not keys_state[keys.UP] and not keys_state[keys.DOWN]:
                self._ship.set_vy(0)

        self._ship_2 = actors.get_first_actor("ship_2")
        if (self._ship_2 != None):
            keys_state = self._keyboard_service.get_keys_state(keys.A, keys.D, keys.S, keys.W)
            if keys_state[keys.A]:
                self._ship_2.set_vx(-VEL)
            if keys_state[keys.D]:
                self._ship_2.set_vx(VEL)
            # if keys_state[keys.S]:
            #     self._ship_2.set_vy(VEL)
            # if keys_state[keys.W]:
            #     self._ship_2.set_vy(-VEL)
            
            if not keys_state[keys.A] and not keys_state[keys.D]:
                self._ship_2.set_vx(0)
            if not keys_state[keys.W] and not keys_state[keys.S]:
                self._ship_2.set_vy(0)

        self._ship_3 = actors.get_first_actor("ship_3")
        if (self._ship_3 != None):
            keys_state = self._keyboard_service.get_keys_state(keys.J, keys.L, keys.K, keys.I)
            # if keys_state[keys.J]:
            #     self._ship_3.set_vx(-VEL)
            # if keys_state[keys.L]:
            #     self._ship_3.set_vx(VEL)
            if keys_state[keys.K]:
                self._ship_3.set_vy(VEL)
            if keys_state[keys.I]:
                self._ship_3.set_vy(-VEL)
            
            if not keys_state[keys.J] and not keys_state[keys.L]:
                self._ship_3.set_vx(0)
            if not keys_state[keys.I] and not keys_state[keys.K]:
                self._ship_3.set_vy(0)

        self._ship_4 = actors.get_first_actor("ship_4")
        if (self._ship_4 != None):
            keys_state = self._keyboard_service.get_keys_state(keys.KP4, keys.KP6, keys.KP5, keys.KP8)
            # if keys_state[keys.KP4]:
            #     self._ship_4.set_vx(-VEL)
            # if keys_state[keys.KP6]:
            #     self._ship_4.set_vx(VEL)
            if keys_state[keys.KP5]:
                self._ship_4.set_vy(VEL)
            if keys_state[keys.KP8]:
                self._ship_4.set_vy(-VEL)

            if not keys_state[keys.KP4] and not keys_state[keys.KP6]:
                self._ship_4.set_vx(0)
            if not keys_state[keys.KP5] and not keys_state[keys.KP8]:
                self._ship_4.set_vy(0)



    # Ship 4 is on the left
    # Ship 3 is on the right
    # Ship 2 is on the top
    # Ship is on the bottom
