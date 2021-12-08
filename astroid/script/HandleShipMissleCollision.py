
from genie.script.action import UpdateAction

class HandleShipMissleCollision(UpdateAction):
    def __init__(self, priority, physics_service, audio_service):
        self._priority = priority
        self._ship_1 = None
        self._ship_2 = None
        self._ship_3 = None
        self._ship_4 = None
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, actors, actions, clock, callback):
        """
            This action handles all collisions between the SHIP and the ASTROIDS
        """
        # First look for the ship
        self._ship_1 = actors.get_first_actor("ship")
        self._ship_2 = actors.get_first_actor("ship_2")
        self._ship_3 = actors.get_first_actor("ship_3")
        self._ship_4 = actors.get_first_actor("ship_4")

        ship_list = [self._ship_1, self._ship_2, self._ship_3, self._ship_4]

        for ship in ship_list:
            if ship is not None:
                for missle in actors.get_actors("missle"):
                    if self._physics_service.check_collision(ship, missle):
                        if ship == self._ship_1:
                            actors.remove_actor("ship", self._ship_1)
                            actors.remove_actor("missle", missle)
                            self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                            self._ship_1 = None
                        elif ship == self._ship_2:
                            actors.remove_actor("ship_2", self._ship_2)
                            actors.remove_actor("missle", missle)
                            self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                            self._ship_2 = None
                        elif ship == self._ship_3:
                            actors.remove_actor("ship_3", self._ship_3)
                            actors.remove_actor("missle", missle)
                            self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                            self._ship_3 = None
                        elif ship == self._ship_4:
                            actors.remove_actor("ship_4", self._ship_4)
                            actors.remove_actor("missle", missle)
                            self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                            self._ship_4 = None


            # Look through the missles and see if any collide with the ship

        # Only worry about collision if the ship actually exists
        # if self._ship != None:
        #     # Look through all the astroids, see if any collides with ship
        #     for actor in actors.get_actors("astroids"):
        #         if self._physics_service.check_collision(self._ship, actor):
        #             actors.remove_actor("ship", self._ship)
        #             actors.remove_actor("astroids", actor)
        #             self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
        #             self._ship = None
        #             break