
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
        self._team_score_1 = 0
        self._team_score_2 = 0

    def execute(self, actors, actions, clock, callback):
        """
            This action handles all collisions between the SHIP and the ASTROIDS
        """
        # First look for the ship
        self._ship_1 = actors.get_first_actor("ship")
        self._ship_2 = actors.get_first_actor("ship_2")
        self._ship_3 = actors.get_first_actor("ship_3")
        self._ship_4 = actors.get_first_actor("ship_4")

        ship_list_team_1 = [self._ship_1, self._ship_3]
        ship_list_team_2 = [self._ship_2, self._ship_4]

        missile_list_team_1 = []
        for missile in actors.get_actors("bullets_1"):
            missile_list_team_1.append(missile)
        for missile in actors.get_actors("bullets_3"):
            missile_list_team_1.append(missile)

        missile_list_team_2 = []
        for missile in actors.get_actors("bullets_2"):
            missile_list_team_2.append(missile)
        for missile in actors.get_actors("bullets_4"):
            missile_list_team_2.append(missile)

        self._team_score_1 = actors.get_first_actor("team_score_1")
        self._team_score_2 = actors.get_first_actor("team_score_2")

        for ship in ship_list_team_1:
            for missle in missile_list_team_2:
                if ship is not None:
                    if self._physics_service.check_collision(ship, missle):
                        self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                        if ship.get_name() == "ship":
                            actors.remove_actor("ship", ship)
                            self._ship_1 = None
                            ship.set_is_dead(True)

                            #math for death
                            total_score_1 = self._team_score_1.get_score()
                            penalty = total_score_1 * 0.1
                            self._team_score_1.penalize(penalty)
                        elif ship.get_name() == "ship_3":
                            actors.remove_actor("ship_3", ship)
                            self._ship_3 = None
                            ship.set_is_dead(True)

                            #math for death
                            total_score_1 = self._team_score_1.get_score()
                            penalty = total_score_1 * 0.1
                            self._team_score_1.penalize(penalty)

        for ship in ship_list_team_2:
            for missle in missile_list_team_1:
                if ship is not None:
                    if self._physics_service.check_collision(ship, missle):
                        self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                        if ship.get_name() == "ship_2":
                            actors.remove_actor("ship_2", ship)
                            self._ship_2 = None
                            ship.set_is_dead(True)

                            #math for death
                            total_score_2 = self._team_score_2.get_score()
                            penalty = total_score_2 * 0.5
                            self._team_score_2.penalize(penalty)
                        elif ship.get_name() == "ship_4":
                            actors.remove_actor("ship_4", ship)
                            self._ship_4 = None
                            ship.set_is_dead(True)

                            #math for death
                            total_score_2 = self._team_score_2.get_score()
                            penalty = total_score_2 * 0.5
                            self._team_score_2.penalize(penalty)
                            

        # for ship in ship_list:
        #     if ship is not None:
        #         for missle in actors.get_actors("bullets"):
        #             if self._physics_service.check_collision(ship, missle):
        #                 if ship == self._ship_1:
        #                     actors.remove_actor("ship", self._ship_1)
        #                     actors.remove_actor("bullets", missle)
        #                     self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
        #                     self._ship_1 = None
        #                 elif ship == self._ship_2:
        #                     actors.remove_actor("ship_2", self._ship_2)
        #                     actors.remove_actor("bullets", missle)
        #                     self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
        #                     self._ship_2 = None
        #                 elif ship == self._ship_3:
        #                     actors.remove_actor("ship_3", self._ship_3)
        #                     actors.remove_actor("bullets", missle)
        #                     self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
        #                     self._ship_3 = None
        #                 elif ship == self._ship_4:
        #                     actors.remove_actor("ship_4", self._ship_4)
        #                     actors.remove_actor("bullets", missle)
        #                     self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
        #                     self._ship_4 = None


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