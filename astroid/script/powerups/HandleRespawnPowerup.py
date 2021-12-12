from random import randint
from genie.script.action import UpdateAction
from astroid.cast.ship import Ship

W_SIZE = (1000, 1000)

class HandleBulletPowerupCollision(UpdateAction):
    def __init__(self, priority, physics_service, audio_service, cast):
        # base stuff for handling updates
        self._priority = priority
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._cast = cast

        # get the ships
        self._ship_1 = None
        self._ship_2 = None
        self._ship_3 = None
        self._ship_4 = None

        #ships extra lives
        self._ship_1_extra = 0
        self._ship_2_extra = 0
        self._ship_3_extra = 0
        self._ship_4_extra = 0


    def execute(self, actors, actions, clock, callback):
            """
                This action handles all collisions between the BULLETS and the RESPAWN_PWR
            """

            self._handle_repsawn_hit(actors)
            self._see_dead()

    def _handle_repsawn_hit(self, actors):
        """
        This method sees if any of the bullets has hit the respawn power up and also checks if
        it has killed the power up. If the power up is killed it adds a life to teammate (if teammate dead)
        or gives the player a life if dead
        """

        # sets the ships and teams for respawn
        self._ship_1 = actors.get_first_actor("ship")
        self._ship_2 = actors.get_first_actor("ship_2")
        self._ship_3 = actors.get_first_actor("ship_3")
        self._ship_4 = actors.get_first_actor("ship_4")

        # First, get a list of bullets out of the cast
        bullets_1 = actors.get_actors("bullets_1")
        bullets_2 = actors.get_actors("bullets_2")
        bullets_3 = actors.get_actors("bullets_3")
        bullets_4 = actors.get_actors("bullets_4")

        for actor in actors.get_actors("respawn_pwr"):
            player_str = "ship_1"
            bullet_str = "bullets_1"
            bullet_var = bullets_1

            teammate_str = "ship_3"
            teamate_var = self._ship_3
           
            collided_bullet = self._physics_service.check_collision_list(actor, bullet_var)
            if collided_bullet != -1:
                actors.remove_actor(bullet_str, collided_bullet)
                actor.take_damage(1)
                self._audio_service.play_sound("astroid/assets/sound/rock_cracking.wav", 0.1)
                
                # If the power up's hp gets down to 0, remove it, 
        
                if (actor.get_hp() <= 0):
                    actors.remove_actor("respawn_pwr", actor)
                    self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                     # adds life to teamate or player
                    if teamate_var == None: # see if teamate is dead and gives them if they are
                        self._add_one_life(teammate_str)
                    else: # gives player extra life if teamate alive
                        self._add_one_life(player_str)

        for actor in actors.get_actors("respawn_pwr"):
            player_str = "ship_2"
            bullet_str = "bullets_2"
            bullet_var = bullets_2

            teammate_str = "ship_4"
            teamate_var = self._ship_4
            
            collided_bullet = self._physics_service.check_collision_list(actor, bullet_var)
            if collided_bullet != -1:
                actors.remove_actor(bullet_str, collided_bullet)
                actor.take_damage(1)
                self._audio_service.play_sound("astroid/assets/sound/rock_cracking.wav", 0.1)
                
                  
        
                if (actor.get_hp() <= 0):
                    actors.remove_actor("respawn_pwr", actor)
                    self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                    
                    if teamate_var == None: # see if teamate is dead and gives them if they are
                        self._add_one_life(teammate_str)
                    else: # gives player extra life if teamate alive
                        self._add_one_life(player_str)

        for actor in actors.get_actors("respawn_pwr"):
            player_str = "ship_3"
            bullet_str = "bullets_3"
            bullet_var = bullets_3

            teammate_str = "ship_1"
            teamate_var = self._ship_1
            
            collided_bullet = self._physics_service.check_collision_list(actor, bullet_var)
            if collided_bullet != -1:
                actors.remove_actor(bullet_str, collided_bullet)
                actor.take_damage(1)
                self._audio_service.play_sound("astroid/assets/sound/rock_cracking.wav", 0.1)
                
                if (actor.get_hp() <= 0):
                    actors.remove_actor("respawn_pwr", actor)
                    self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                    
                    if teamate_var == None: # see if teamate is dead and gives them if they are
                        self._add_one_life(teammate_str)
                    else: # gives player extra life if teamate alive
                        self._add_one_life(player_str)

        for actor in actors.get_actors("respawn_pwr"):
                player_str = "ship_4"
                bullet_str = "bullets_4"
                bullet_var = bullets_4

                teammate_str = "ship_2"
                teamate_var = self._ship_2

                collided_bullet = self._physics_service.check_collision_list(actor, bullet_var)
                if collided_bullet != -1:
                    actors.remove_actor(bullet_str, collided_bullet)
                    actor.take_damage(1)
                    self._audio_service.play_sound("astroid/assets/sound/rock_cracking.wav", 0.1)
                    
            
                    if (actor.get_hp() <= 0):
                        actors.remove_actor("respawn_pwr", actor)
                        self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)
                        
                        if teamate_var == None: # see if teamate is dead and gives them if they are
                            self._add_one_life(teammate_str)
                        else: # gives player extra life if teamate alive
                            self._add_one_life(player_str)

    def _add_one_life(self, player):
        if player == "ship_1":
            self._ship_1_extra += 1
        elif player == "ship_2":
            self._ship_2_extra += 1
        elif player == "ship_3":
            self._ship_3_extra += 1
        elif player == "ship_4":
            self._ship_4_extra += 1

    def _see_dead(self):
        if self._ship_1 == None:
            if self._ship_1_extra > 0:
                self._respawn_player("ship_1")
                self._ship_1_extra -= 1

        if self._ship_2 == None:
            if self._ship_2_extra > 0:
                self._respawn_player("ship_2")
                self._ship_2_extra -= 1

        if self._ship_3 == None:
            if self._ship_3_extra > 0:
                self._respawn_player("ship_3")
                self._ship_3_extra -= 1

        if self._ship_4 == None:
            if self._ship_4_extra > 0:
                self._respawn_player("ship_4")
                self._ship_4_extra -= 1
    
    def _respawn_player(self, player):
        
        ran_x = randint(W_SIZE[0] * .2, W_SIZE[0] * .8) # for random horzantal spawn
        ran_y = randint(W_SIZE[1] * .2, W_SIZE[1] * .8) # for random vertical spawn

        if player == "ship_1" and self._ship_1 == None:
            local_x = ran_x
            local_y = W_SIZE[1]/10 * 9
            local_rotation = 180

            self._ship_1 = Ship(path="astroid/assets/spaceship/spaceship_yellow.png", 
                width = 70,
                height = 50,
                x = local_x,
                y = local_y,
                rotation=local_rotation)
            self._ship_1.set_name("ship_1")
            self._ship_1.set_team("yellow")
            self._cast.add_actor("ship_1", self._ship_1)
        elif player == "ship_2" and self._ship_2 == None:
            local_x = ran_x
            local_y = W_SIZE[1]/10
            local_rotation = 0

            self._ship_2 = Ship(path="astroid/assets/spaceship/spaceship_red.png", 
                width = 70,
                height = 50,
                x = local_x,
                y = local_y,
                rotation=local_rotation)
            self._ship_2.set_name("ship_2")
            self._ship_2.set_team("red")
            self._cast.add_actor("ship_2", self._ship_2)
        elif player == "ship_3" and self._ship_3 == None:
            local_x = W_SIZE[0]/10 * 9
            local_y = ran_y
            local_rotation = 90

            self._ship_3 = Ship(path="astroid/assets/spaceship/spaceship_yellow.png", 
                width = 70,
                height = 50,
                x = local_x,
                y = local_y,
                rotation=local_rotation)
            self._ship_3.set_name("ship_3")
            self._ship_3.set_team("yellow")
            self._cast.add_actor("ship_3", self._ship_3)
        elif player == "ship_4" and self._ship_4 == None:
            local_x = W_SIZE[0]/10
            local_y = ran_y
            local_rotation = 270

            self._ship_4 = Ship(path="astroid/assets/spaceship/spaceship_red.png", 
                width = 70,
                height = 50,
                x = local_x,
                y = local_y,
                rotation=local_rotation)
            self._ship_4.set_name("ship_4")
            self._ship_4.set_team("red")
            self._cast.add_actor("ship_4", self._ship_4)
        
