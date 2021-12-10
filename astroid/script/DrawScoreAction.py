from genie.script.action import OutputAction
from genie.services import colors
from astroid.cast.ship import Ship

W_SIZE = (1000, 1000)

class DrawScoreAction(OutputAction):
    def __init__(self, priority, screen_service, cast):
        super().__init__(priority)
        self._score_1 = None
        self._score_2 = None
        self._screen_service = screen_service
        self._ship_1 = None
        self._ship_2 = None
        self._ship_3 = None
        self._ship_4 = None
        self._cast = cast

    def get_priority(self):
        return super().get_priority()
    
    def set_priority(self, priority):
        return super().set_priority(priority)

    def execute(self, actors, actions, clock, callback):
        """
            - Look for the score actor in the actors list
            - Print the score on the screen
        """
        if (self._score_2 == None):
            self._score_2 = actors.get_first_actor("team_score_2")
            # for actor in actors:
            #     if isinstance(actor, PlayerScore):
            #         self._score = actor
            #         break
        if self._score_2 != None:
            self._screen_service.draw_text("Score: " + str(self._score_2.get_score()), font_size=48, color=colors.WHITE, position= (20,20))

        if (self._score_1 == None):
            self._score_1 = actors.get_first_actor("team_score_1")
            # for actor in actors:
            #     if isinstance(actor, PlayerScore):
            #         self._score = actor
            #         break
        if self._score_1 != None:
            self._screen_service.draw_text("Score: " + str(self._score_1.get_score()), font_size=48, color=colors.WHITE, position= (700,900))

        self._ship_1 = actors.get_first_actor("ship")
        self._ship_2 = actors.get_first_actor("ship_2")
        self._ship_3 = actors.get_first_actor("ship_3")
        self._ship_4 = actors.get_first_actor("ship_4")

        if self._ship_1 == None and self._ship_3 == None:
            team_1_dead = True
        else:
            team_1_dead = False

        if self._ship_2 == None and self._ship_4 == None:
            team_2_dead = True
        else:
            team_2_dead = False

        # Respawn
        if self._ship_1 == None:
            if self._score_1.get_score() >= 75:
                self._score_1.set_score(self._score_1.get_score() * .5)
                # Bottom
                self._ship_1 = Ship(path="astroid/assets/spaceship/spaceship_yellow.png", 
                    width = 70,
                    height = 50,
                    x = W_SIZE[0]/2,
                    y = W_SIZE[1]/10 * 9,
                    # y = mother_ship.get_top_left()[1] - 30,
                    rotation=180)
                self._ship_1.set_name("ship")
                self._ship_1.set_team("yellow")
                self._cast.add_actor("ship", self._ship_1)
                
                

        if self._ship_2 == None:
            if self._score_2.get_score() >= 75:
                self._score_2.set_score(self._score_2.get_score() * .5)
                # Top
                self._ship_2 = Ship(path="astroid/assets/spaceship/spaceship_red.png", 
                    width = 70,
                    height = 50,
                    x = W_SIZE[0]/2,
                    y = W_SIZE[1]/10 ,
                    # y = mother_ship.get_top_left()[1] - 30,
                    rotation=0)
                self._ship_2.set_name("ship_2")
                self._ship_2.set_team("red")
                self._cast.add_actor("ship_2", self._ship_2)

        if self._ship_3 == None:
            if self._score_1.get_score() >= 75:
                self._score_1.set_score(self._score_1.get_score() * .5)
                # Right
                self._ship_3 = Ship(path="astroid/assets/spaceship/spaceship_yellow.png", 
                    width = 70,
                    height = 50,
                    x = W_SIZE[0]/10 * 9,
                    y = W_SIZE[1]/2,
                    # y = mother_ship.get_top_left()[1] - 30,
                    rotation=90)
                self._ship_3.set_name("ship_3")
                self._ship_3.set_team("yellow")
                self._cast.add_actor("ship_3", self._ship_3)

        if self._ship_4 == None:
            if self._score_2.get_score() >= 75:
                self._score_2.set_score(self._score_2.get_score() * .5)
                # Left
                self._ship_4 = Ship(path="astroid/assets/spaceship/spaceship_red.png", 
                    width = 70,
                    height = 50,
                    x = W_SIZE[0]/10,
                    y = W_SIZE[1]/2,
                    # y = mother_ship.get_top_left()[1] - 30,
                    rotation=270)
                self._ship_4.set_name("ship_4")
                self._ship_4.set_team("red")
                self._cast.add_actor("ship_4", self._ship_4)

        if (self._score_1.get_score() <= 0 or self._score_2.get_score() <= 0) or (team_1_dead == True or team_2_dead == True) or (self._score_1.get_score() >= 100 or self._score_2.get_score() >= 100):
            self._screen_service.draw_text("GAME OVER", font_size=48, color=colors.WHITE, position= (350,500)) 

        

          