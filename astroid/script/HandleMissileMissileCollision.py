from genie.script.action import UpdateAction

class HandleBulletsBulletsCollision(UpdateAction):
    def __init__(self, priority, physics_service, audio_service):
        self._priority = priority
        self._score = None
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, actors, actions, clock, callback):
        """
            This action handles all collisions between the BULLETS and the ASTROIDS
        """
        # If we don't know who's the score actor, find it
        self._score = actors.get_first_actor("score")
        
        # First, get a list of bullets out of the cast
        bullets_1 = actors.get_actors("bullets_1")
        bullets_2 = actors.get_actors("bullets_2")
        bullets_3 = actors.get_actors("bullets_3")
        
        #Next, loop through all the astroids to see which one collides with
        #any of the bullets
        for actor in actors.get_actors("bullets_2"):
        # if isinstance(actor, Astroid):
            collided_bullet = self._physics_service.check_collision_list(actor, bullets_1)
            if collided_bullet != -1:
                actors.remove_actor("bullets_1", collided_bullet)
                actors.remove_actor("bullets_2", actor)
                self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)

        #Next, loop through all the astroids to see which one collides with
        #any of the bullets
        for actor in actors.get_actors("bullets_3"):
        # if isinstance(actor, Astroid):
            collided_bullet = self._physics_service.check_collision_list(actor, bullets_1)
            if collided_bullet != -1:
                actors.remove_actor("bullets_1", collided_bullet)
                actors.remove_actor("bullets_3", actor)
                self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)

        #Next, loop through all the astroids to see which one collides with
        #any of the bullets
        for actor in actors.get_actors("bullets_4"):
        # if isinstance(actor, Astroid):
            collided_bullet = self._physics_service.check_collision_list(actor, bullets_1)
            if collided_bullet != -1:
                actors.remove_actor("bullets_1", collided_bullet)
                actors.remove_actor("bullets_4", actor)
                self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)

        #Next, loop through all the astroids to see which one collides with
        #any of the bullets
        for actor in actors.get_actors("bullets_3"):
        # if isinstance(actor, Astroid):
            collided_bullet = self._physics_service.check_collision_list(actor, bullets_2)
            if collided_bullet != -1:
                actors.remove_actor("bullets_2", collided_bullet)
                actors.remove_actor("bullets_3", actor)
                self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)

        #Next, loop through all the astroids to see which one collides with
        #any of the bullets
        for actor in actors.get_actors("bullets_4"):
        # if isinstance(actor, Astroid):
            collided_bullet = self._physics_service.check_collision_list(actor, bullets_2)
            if collided_bullet != -1:
                actors.remove_actor("bullets_2", collided_bullet)
                actors.remove_actor("bullets_4", actor)
                self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)

        #Next, loop through all the astroids to see which one collides with
        #any of the bullets
        for actor in actors.get_actors("bullets_4"):
        # if isinstance(actor, Astroid):
            collided_bullet = self._physics_service.check_collision_list(actor, bullets_3)
            if collided_bullet != -1:
                actors.remove_actor("bullets_3", collided_bullet)
                actors.remove_actor("bullets_4", actor)
                self._audio_service.play_sound("astroid/assets/sound/explosion-01.wav", 0.1)

                