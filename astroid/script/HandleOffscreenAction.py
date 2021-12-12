
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
        self._astroids = None
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
        self._astroids = actors.get_actors("astroids")
        self._pwr_ups = actors.get_actors("respawn_pwr")
        
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
        
        for astroid in self._astroids:
            # will keep the astroids or the enemies within the play box
            if astroid != None:

                # this is reversing the velocity so they stay within the play box

                if astroid.get_x() >= self._window_size[0] * .8:
                    vx = astroid.get_vx()
                    astroid.set_vx(vx * -1)
                if astroid.get_x() <= self._window_size[0] * .2:
                    vx = astroid.get_vx()
                    astroid.set_vx(vx * -1)
                if astroid.get_y() >= self._window_size[1] * .8:
                    vy = astroid.get_vy()
                    astroid.set_vy(vy * -1)
                if astroid.get_y() <= self._window_size[1] * .2:
                    vy = astroid.get_vy()
                    astroid.set_vy(vy * -1)

        for pwr_up in self._pwr_ups:
            # will keep the astroids or the enemies within the play box
            if pwr_up != None:

                # this is reversing the velocity so they stay within the play box

                if pwr_up.get_x() >= self._window_size[0] * .8:
                    vx = pwr_up.get_vx()
                    pwr_up.set_vx(vx * -1)
                if pwr_up.get_x() <= self._window_size[0] * .2:
                    vx = pwr_up.get_vx()
                    pwr_up.set_vx(vx * -1)
                if pwr_up.get_y() >= self._window_size[1] * .8:
                    vy = pwr_up.get_vy()
                    pwr_up.set_vy(vy * -1)
                if pwr_up.get_y() <= self._window_size[1] * .2:
                    vy = pwr_up.get_vy()
                    pwr_up.set_vy(vy * -1)

        # If it's a astroid going off the screen, just remove it.
        for actor in actors.get_actors("astroids"):
            # if isinstance(actor, Astroid)
            if (actor.get_x() > self._window_size[0]
                or actor.get_x() < 0
                or actor.get_y() > self._window_size[1]
                or actor.get_y() < 0):
                actors.remove_actor("astroids", actor)


        # Delete all the missles off screen
        for missile in actors.get_actors("bullets_1"):
            if (missile.get_x() > self._window_size[0]
                or missile.get_x() < 0
                or missile.get_y() > self._window_size[1]
                or missile.get_y() < 0):
                actors.remove_actor("bullets_1", missile)

        for missile in actors.get_actors("bullets_2"):
            if (missile.get_x() > self._window_size[0]
                or missile.get_x() < 0
                or missile.get_y() > self._window_size[1]
                or missile.get_y() < 0):
                actors.remove_actor("bullets_2", missile)

        for missile in actors.get_actors("bullets_3"):
            if (missile.get_x() > self._window_size[0]
                or missile.get_x() < 0
                or missile.get_y() > self._window_size[1]
                or missile.get_y() < 0):
                actors.remove_actor("bullets_3", missile)

        for missile in actors.get_actors("bullets_4"):
            if (missile.get_x() > self._window_size[0]
                or missile.get_x() < 0
                or missile.get_y() > self._window_size[1]
                or missile.get_y() < 0):
                actors.remove_actor("bullets_4", missile)