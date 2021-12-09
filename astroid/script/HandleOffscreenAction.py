
from astroid.cast.astroid import Astroid
from genie.script.action import UpdateAction

class HandleOffscreenAction(UpdateAction):
    def __init__(self, priority,  window_size):
        super().__init__(priority)
        self._window_size = window_size
        self._play_box_x = window_size[0] * .8
        self._play_box_y = window_size[1] * .8
        self._ship = None
        self._ship_2 = None
        self._ship_3 = None
        self._ship_4 = None
        self._astroid = None
        self._mother_ship = None

    def execute(self, actors, actions, clock, callback):
        """
            Handle all actors' behavior when they're about to
            go off the screen
        """
        # Look for the ship
        self._ship = actors.get_first_actor("ship")
        self._ship_2 = actors.get_first_actor("ship_2")
        self._ship_3 = actors.get_first_actor("ship_3")
        self._ship_4 = actors.get_first_actor("ship_4")
        self._astroid = actors.get_first_actor("astroids")
        
        # Don't allow the ship to go off the screen
        if (self._ship != None):
            if self._ship.get_top_right()[0] >= self._window_size[0] * .9 - 40:
                self._ship.set_x(int((self._window_size[0] * .9 - 40) - self._ship.get_width()/2))
            if self._ship.get_top_left()[0] <= self._window_size[0] * .1 + 40:
                self._ship.set_x(int((self._window_size[0] * .1 + 40) + self._ship.get_width()/2))
            # if self._ship.get_bottom_left()[1] >= self._window_size[1]:
            #     self._ship.set_y(int((self._window_size[1] * .8) - self._ship.get_height()/2))
            # if self._ship.get_top_left()[1] <= 0:
            #     self._ship.set_y(int(self._ship.get_height()/2))

        if (self._ship_2 != None):
            if self._ship_2.get_top_right()[0] >= self._window_size[0] * .9 - 40:
                self._ship_2.set_x(int((self._window_size[0] * .9 - 40) - self._ship_2.get_width()/2))
            if self._ship_2.get_top_left()[0] <= self._window_size[0] * .1 + 40:
                self._ship_2.set_x(int((self._window_size[0] * .1 + 40) + self._ship_2.get_width()/2))
            # if self._ship_2.get_bottom_left()[1] >= self._window_size[1]:
            #     self._ship_2.set_y(int(self._window_size[1] - self._ship_2.get_height()/2))
            # if self._ship_2.get_top_left()[1] <= 0:
            #     self._ship_2.set_y(int(self._ship_2.get_height()/2))

        if (self._ship_3 != None):
            # if self._ship_3.get_top_right()[0] >= self._window_size[0]:
            #     self._ship_3.set_x(int(self._window_size[0] - self._ship_3.get_width()/2))
            # if self._ship_3.get_top_left()[0] <= 0:
            #     self._ship_3.set_x(int(self._ship_3.get_width()/2))
            if self._ship_3.get_bottom_left()[1] >= self._window_size[1] * .9 - 50:
                self._ship_3.set_y(int(self._window_size[1] *.9 - 50 - self._ship_3.get_height()/2))
            if self._ship_3.get_top_left()[1] <= self._window_size[0] * .1 + 55:
                self._ship_3.set_y(int((self._window_size[0] * .1 + 45) + self._ship_3.get_width()/2))
                
        if (self._ship_4 != None):
            # if self._ship_4.get_top_right()[0] >= self._window_size[0]:
            #     self._ship_4.set_x(int(self._window_size[0] - self._ship_4.get_width()/2))
            # if self._ship_4.get_top_left()[0] <= 0:
            #     self._ship_4.set_x(int(self._ship_4.get_width()/2))
            if self._ship_4.get_bottom_left()[1] >= self._window_size[1] * .9 - 50:
                self._ship_4.set_y(int(self._window_size[1] *.9 - 50 - self._ship_4.get_height()/2))
            if self._ship_4.get_top_left()[1] <= self._window_size[0] * .1 + 55:
                self._ship_4.set_y(int((self._window_size[0] * .1 + 45) + self._ship_4.get_width()/2))
        
        # will keep the astroids or the enemies within the play box
        if self._astroid != None:

            # this is reversing the velocity so they stay within the play box

            if self._astroid.get_x() >= self._window_size[0] * .8 :
                vx = self._astroid.get_vx()
                self._astroid.set_vx(vx * -1)
            if self._astroid.get_x() <= self._window_size[0] * .2:
                vx = self._astroid.get_vx()
                self._astroid.set_vx(vx * -1)
            if self._astroid.get_y() >= self._window_size[1] * .8:
                vy = self._astroid.get_vy()
                self._astroid.set_vy(vy * -1)
            if self._astroid.get_y() <= self._window_size[1] * .2:
                vy = self._astroid.get_vy()
                self._astroid.set_vy(vy * -1)
        # If it's a bullet or astroid goin off the screen, just remove it.
        for actor in actors.get_actors("astroids"):
            # if isinstance(actor, Astroid) or isinstance(actor, Bullet):
            if (actor.get_x() > self._window_size[0]
                or actor.get_x() < 0
                or actor.get_y() > self._window_size[1]
                or actor.get_y() < 0):
                actors.remove_actor("astroids", actor)