#!/usr/bin/env python3

# Created by: Lily Carroll
# This program is the "Stellar Showdown" program on the PyBadge.
# Importing Circuit Python libraries.
import random
import time
import constants
import stage
import ugame


# This function is for my splash game scene.
def splash_scene():
    # Need to also download the sound file onto the PyBadge.
    # Sound that will play when the splash scene is displayed on PyBadge.
    coin_sound = open("coin.wav", "rb")
    # To allow for the use of sound objects (audio).
    sound = ugame.audio
    # Stopping the sound.
    sound.stop()
    # Not allowing for the sound to be muted.
    sound.mute(False)
    # Playing the sound from the file.
    sound.play(coin_sound)

    # Importing background image (White Screen).
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Adding a grid background image that is 10x8.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # Used this program to split the image into tile:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # Game variable which will display on the PyBadge and refresh it with 60 hertz.
    game = stage.Stage(ugame.display, constants.FPS)

    # Adding images from our files that were downloaded to a list to display them on the PyBadge.
    game.layers = [background]

    # Adding the game variable to the game scene.
    game.render_block()

    # Using a while True loop to repeat my game forever until the user turns it off (gaming loop).
    while True:
        # Waiting 2 seconds before going to the menu scene.
        time.sleep(2.0)
        menu_scene()


# This function is for my menu game scene.
def menu_scene():
    # Importing background image (White Screen).
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Adding the text objects.
    # Creating a list called text.
    text = []
    # Created text1 variable which allows us to style our writing that will display on the menu scene.
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALLETTE, buffer=None
    )
    # Displaying the text 20 pixels over and 10 pixels down from the origin.
    text1.move(20, 10)
    # Text message that is displayed.
    text1.text("LC Studios")
    # Appending the text message to the list.
    text.append(text1)

    # Created text2 variable which allows us to style our writing that will display on the menu scene.
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALLETTE, buffer=None
    )
    # Displaying the text 40 pixels over and 110 pixels down from the origin.
    text2.move(40, 110)
    # Text message that is displayed.
    text2.text("PRESS START")
    # Appending the second text message to the list.
    text.append(text2)

    # Adding a grid background image that is 10x8.
    background = stage.Grid(image_bank_background, 10, 8)

    # Game variable which will display on the PyBadge and refresh it with 60 hertz.
    game = stage.Stage(ugame.display, 60)

    # Adding images from our files that were downloaded to a list to display them on the PyBadge.
    game.layers = text + [background]

    # Adding the game variable to the game scene.
    game.render_block()

    # Using a while True loop to repeat my game forever until the user turns it off (gaming loop).
    while True:
        # Going to get user input.
        # Figuring out what buttons are being pressed on the PyBadge.
        keys = ugame.buttons.get_pressed()

        # If the START button is being pressed then go to game_scene().
        if keys & ugame.K_START != 0:
            game_scene()

        # This will guarantee that we have a 60 second refresh rate for the background.
        game.tick()


def game_scene():
    # Function that will remove an alien off the screen anf put it onto the screen.
    def show_alien():
        # Using a for loop to check through all the aliens.
        for alien_number in range(len(aliens)):
            # Using an if statement to check if an alien has a negative x position.
            if aliens[alien_number].x < 0:
                # If the alien does exist move to a random x loaction on the screen and the y location is the same.
                aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
            # Breaking out of loop.
            break

        # Importing background image.
        image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
        # Importing sprite image.
        image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

        # Buttons that will not change its information/task.
        # When the game starts none of these buttons are being pressed (button_up).
        a_button = constants.button_state["button_up"]
        b_button = constants.button_state["button_up"]
        start_button = constants.button_state["button_up"]
        select_button = constants.button_state["button_up"]

        # Creating a sound variable that will take the sound from my pew.wav file and assign it to the sound variable.
        pew_sound = open("pew.wav", "rb")
        # To allow for the use of sound objects (audio).
        sound = ugame.audio
        # Stopping the sound.
        sound.stop()
        # Not allowing for the sound to be muted.
        sound.mute(False)

        # Created a grid for the image background, that is 10x8 of the 16x16 images in it.
        background = stage.Grid(
            image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
        )

        # For loop that will move along the x-axis inside the constant SCREEN_GRID_X (10 pixels in total).
        for x_location in range(constants.SCREEN_GRID_X):
            # Nested for loop that will move along the y-axis inside the constant SCREEN_GRID_Y (8 pixels in total).
            for y_location in range(constants.SCREEN_GRID_Y):
                tile_picked = random.randint(1, 3)
                background.tile(x_location, y_location, tile_picked)

        # Creating a single sprite which will display the 5th image in the file (ship).
        # It will display 75 pixels to the right of the origin and 66 pixels down.
        ship = stage.Sprite(
            image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
        )

        # Creating another sprite which will display from the 9th image in the file (alien).
        # It will display in the middle of the screen and 16 pixels down from the top of the screen.
        # Declaring a list of aliens.
        aliens = []
        # Using a For loop to go through the 5 aliens.
        for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
            # Creating a single alien which will display from the 9th image bank.
            # Setting it's coordinates off the screen.
            a_single_alien = stage.Sprite(
                image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
            )

            # Appending each alien to the list.
            aliens.append(a_single_alien)

        # Placling 1 alien onto the screen.
        show_alien()

        # Creating multiple laser sprites.
        # Declaring a list for the 5 lasers.
        lasers = []
        # Using a For loop to create a new Sprite object from 0 lasers in the game to 8 lasers.
        for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
            # Create a single laser sprite using the 10th image in the image bank and using these coordinates.
            a_single_laser = stage.Sprite(
                image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
            )
            # Appending the single laser to the list.
            lasers.append(a_single_laser)

        # Game variable which will display on the PyBadge and refresh it with 60 hertz.
        game = stage.Stage(ugame.display, 60)

        # Adding images to a list to display the first image in the pbm file.
        game.layers = lasers + [ship] + aliens + [background]

        # Adding the game variable to the game scene.
        game.render_block()

        # Using a while True loop to repeat my game forever until the user turns it off (gaming loop).
        while True:
            # Going to get user input.
            # Figuring out what buttons are being pressed on the PyBadge.
            keys = ugame.buttons.get_pressed()

            # If the A button is being pressed then it returns "A".
            if keys & ugame.K_X != 0:
                # Using an if statement for when a button was just up but is now being pressed.
                if a_button == constants.button_state["button_up"]:
                    a_button = constants.button_state["button_just_pressed"]
                # Using am elif for when the button was already pressed and is still being pressed.
                elif a_button == constants.button_state["button_just_pressed"]:
                    a_button = constants.button_state["button_still_pressed"]
            # Else the "A" button wasn't pressed.
            else:
                # Using an if statement for if the button is still being pressed then classify the button as in its just released state.
                if a_button == constants.button_state["button_still_pressed"]:
                    a_button = constants.button_state["button_released"]
                # If it wasn't still being pressed then that means the button is up (not being pressed).
                else:
                    a_button = constants.button_state["button_up"]

            # If the B button is being pressed then it returns "B".
            if keys & ugame.K_O:
                pass

            # If the START button is being pressed then it returns "Start".
            if keys & ugame.K_START != 0:
                pass

            # If the SELECT button is being pressed then it returns "Select".
            if keys & ugame.K_SELECT != 0:
                pass
            # If the right button is being pressed then it moves the ship right (by 1 pixel) from its current position along the x direction.
            if keys & ugame.K_RIGHT != 0:
                # Using an if statement to check if the ship's position is less than or equal to 160 pixels then we can move the ship over.
                if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                    ship.move(ship.x + 1, ship.y)
                    # Otherwise set it to 0 to keep the ship from moving off the screen.
                else:
                    ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

            # If the left button is being pressed then it moves the ship left (by 1 pixel) from its current position along the y direction.
            if keys & ugame.K_LEFT != 0:
                # Using an if statement to allow the ship to go right up to the edge of the Pybadge screen.
                if ship.x >= 0:
                    ship.move(ship.x - 1, ship.y)
                # Otherwise set it to 0 to keep the ship from moving off the screen.
                else:
                    ship.move(0, ship.y)

            # If the up button is being pressed it moves the ship up (by 1 pixel) by decreasing the y direction.
            if keys & ugame.K_UP != 0:
                pass

            # If the down button is being pressed it moves the ship down (by 1 pixel) by increasing the y direction.
            if keys & ugame.K_DOWN != 0:
                pass

            # Updating user game logic to proceed to the next step once the user carries out an action.
            # Using an if statement for when the button was just pressed, play the pew sound.
            if a_button == constants.button_state["button_just_pressed"]:
                # Firing lasers from our range of lasers 0-5.
                for laser_number in range(len(lasers)):
                    # Check each of the lasers x coordinate is less than 0.
                    if lasers[laser_number].x < 0:
                        # Laser that is off the screen and move it to the ship sprite's coordinates.
                        lasers[laser_number].move(ship.x, ship.y)
                        # Play the pew sound.
                        sound.play(pew_sound)
                        # Break if there is ever a single laser that needs to be moved over onto the screen.
                        break

            # For loop to again loop through all of our lasers.
            for laser_number in range(len(lasers)):
                # Using an if statement to check if the laser is on the screen.
                if lasers[laser_number].x > 0:
                    # Then move the laser up 1 pixel by decreasing its y coordinate by 2 since y direction increases as you move down.
                    lasers[laser_number].move(
                        lasers[laser_number].x,
                        lasers[laser_number].y - constants.LASER_SPEED,
                    )
                    # Using an if statement to check if it's y location is less than off the top of the screen.
                    if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                        # Then move the laser back to that starting point (both negative x and y coordinates).
                        lasers[laser_number].move(
                            constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                        )
            # For loop to go through the list of aliens.
            for alien_number in range(len(aliens)):
                # Using an if statement to check if the alien is on the screen.
                if aliens[alien_number].x > 0:
                    # Then move the alien pixel down by 1 pixel.
                    aliens[alien_number].move(
                        aliens[alien_number].x,
                        aliens[alien_number].y + constants.ALIEN_SPEED,
                    )
                    # Checking if an alien has moved off the screen, then move it back onto the screen.
                    if aliens[alien_number].y > constants.SCREEN_Y:
                        aliens[alien_number].move(
                            constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                        )
                        # Calling show_alien function.
                        show_alien()

                        # Redraw sprites to move the sprite around and not affect the background which will not change.
            game.render_sprites(lasers + [ship] + aliens)
            # Will wait until one 60th of a second has happened and then re-loop.
            # This will guarantee that we have a 60 second refresh rate for the background.
            game.tick()


if __name__ == "__main__":
    splash_scene()
