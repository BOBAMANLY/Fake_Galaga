from genie.director import Director
from genie.cast.cast import Cast
from genie.script.script import Script
from genie.services import *

from astroid.cast.ship import Ship
from astroid.cast.background import Background
from astroid.cast.startGameButton import StartGameButton
from astroid.cast.play_box import Play_box

from astroid.script.HandleQuitAction import HandleQuitAction
from astroid.script.HandleShipMovementAction import HandleShipMovementAction
from astroid.script.HandleShootingAction import HandleShootingAction
from astroid.script.HandleStartGameAction import HandleStartGameAction

from astroid.script.MoveActorsAction import MoveActorsAction
from astroid.script.SpawnEnemiesAction import SpawnEnemiesAction
from astroid.script.HandleOffscreenAction import HandleOffscreenAction
from astroid.script.HandleShipMissleCollision import HandleShipMissleCollision
from astroid.script.HandleBulletsAstroidsCollision import HandleBulletsAstroidsCollision
from astroid.script.HandleMissileMissileCollision import HandleBulletsBulletsCollision

from astroid.script.DrawActorsAction import DrawActorsAction
from astroid.script.UpdateScreenAction import UpdateScreenAction

from astroid.cast.team_score import Team_Score

from astroid.script.DrawScoreAction import DrawScoreAction

from astroid.script.powerups.SpawnRespawnPowerup import SpawRespawnPwrAction
from astroid.script.powerups.HandleRespawnPowerup import HandleBulletPowerupCollision


W_SIZE = (1000, 1000)
START_POSITION = 200, 250
SHIP_WIDTH = 40
SHIP_LENGTH = 55
SCREEN_TITLE = "Multi-Galaga"
# 
def get_services():
    """
        Ask the user whether they want to use pygame or raylib services
    """
    return {
    "keyboard" : RaylibKeyboardService(),
    "physics" : RaylibPhysicsService(),
    "screen" : RaylibScreenService(W_SIZE, SCREEN_TITLE),
    "audio" : RaylibAudioService(),
    "mouse" : RaylibMouseService()
    }

def main():
    """
        Create director, cast, script, then run the game loop
    """
    # Get all the services needed services 
    services = get_services()

    keyboard_service = services["keyboard"]
    physics_service = services["physics"]
    screen_service = services["screen"]
    audio_service = services["audio"]
    mouse_service = services["mouse"]

    # Create a director
    director = Director()

    # Create all the actors, including the player
    cast = Cast()

    # Create the players

    # Bottom
    ship = Ship(path="astroid/assets/spaceship/spaceship_yellow.png", 
                    width = 70,
                    height = 50,
                    x = W_SIZE[0]/2,
                    y = W_SIZE[1]/10 * 9,
                    # y = mother_ship.get_top_left()[1] - 30,
                    rotation=180)
    ship.set_name("ship")
    ship.set_team("yellow")
    
    # Top
    ship_2 = Ship(path="astroid/assets/spaceship/spaceship_red.png", 
                    width = 70,
                    height = 50,
                    x = W_SIZE[0]/2,
                    y = W_SIZE[1]/10 ,
                    # y = mother_ship.get_top_left()[1] - 30,
                    rotation=0)
    ship_2.set_name("ship_2")
    ship_2.set_team("red")

    # Right
    ship_3 = Ship(path="astroid/assets/spaceship/spaceship_yellow.png", 
                    width = 70,
                    height = 50,
                    x = W_SIZE[0]/10 * 9,
                    y = W_SIZE[1]/2,
                    # y = mother_ship.get_top_left()[1] - 30,
                    rotation=90)
    ship_3.set_name("ship_3")
    ship_3.set_team("yellow")
    
    # Left
    ship_4 = Ship(path="astroid/assets/spaceship/spaceship_red.png", 
                    width = 70,
                    height = 50,
                    x = W_SIZE[0]/10,
                    y = W_SIZE[1]/2,
                    # y = mother_ship.get_top_left()[1] - 30,
                    rotation=270)
    ship_4.set_name("ship_4")
    ship_4.set_team("red")

    # Scale the background to have the same dimensions as the Window,
    # then position it at the center of the screen
    background_image = Background("astroid/assets/space.png", 
                                    width=W_SIZE[0],
                                    height=W_SIZE[1],
                                    x = W_SIZE[0]/2,
                                    y = W_SIZE[1]/2)

    # adding the play box

    play_box = Play_box("astroid/assets/play_box.png", width=W_SIZE[0]* .8, height=W_SIZE[1]* .8, x = W_SIZE[0]/2, y = W_SIZE[1]/2)

    # Start game button
    start_button = StartGameButton(path="astroid/assets/others/start_button.png",
                                    width = 305,
                                    height = 113,
                                    x = W_SIZE[0]/2,
                                    y = W_SIZE[1]/2)

    # Give actor(s) to the cast
    cast.add_actor("background_image", background_image)
    cast.add_actor("ship", ship)
    cast.add_actor("ship_2", ship_2)
    cast.add_actor("ship_3", ship_3)
    cast.add_actor("ship_4", ship_4)
    cast.add_actor("start_button", start_button)
    cast.add_actor("play_box", play_box)

    score_1 = Team_Score(path="", score = 50)
    score_2 = Team_Score(path="", score = 50)
    cast.add_actor("team_score_1", score_1)
    cast.add_actor("team_score_2", score_2)


    # Create all the actions
    script = Script()

    # Create input actions
    script.add_action("input", HandleQuitAction(1, keyboard_service))

    # Add actions that must be added to the script when the game starts
    startgame_actions = {"input" : [], "update" : [], "output": []}
    startgame_actions["input"].append(HandleShootingAction(1, keyboard_service, audio_service))
    startgame_actions["input"].append(HandleShipMovementAction(2, keyboard_service))
    startgame_actions["update"].append(SpawnEnemiesAction(1, W_SIZE))
    script.add_action("input", HandleStartGameAction(2, mouse_service, physics_service, startgame_actions))

    # Create update actions
    script.add_action("update", MoveActorsAction(1, physics_service))
    script.add_action("update", HandleOffscreenAction(1, W_SIZE))
    script.add_action("update", HandleShipMissleCollision(1, physics_service, audio_service))
    script.add_action("update", HandleBulletsAstroidsCollision(1, physics_service, audio_service))
    script.add_action("update", HandleBulletsBulletsCollision(1, physics_service, audio_service))
    script.add_action("update", SpawRespawnPwrAction(1,W_SIZE))
    script.add_action("update", HandleBulletPowerupCollision(1, physics_service, audio_service, cast))

    # Create output actions
    script.add_action("output", DrawActorsAction(1, screen_service))
    script.add_action("output", DrawScoreAction(1, screen_service, cast))
    script.add_action("output", UpdateScreenAction(2, screen_service))


    # Give the cast and script to the dirrector by calling direct_scene.
    # direct_scene then runs the main game loop:
    director.direct_scene(cast, script)

if __name__ == "__main__":
    main()