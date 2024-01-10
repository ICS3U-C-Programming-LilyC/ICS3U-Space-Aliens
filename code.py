#!/usr/bin/env python3

# Created by: Lily Carroll
# This program is the "Dino Blaster" program on the PyBadge.
# Importing Circuit Python libraries.
import stage
import ugame


# This function is for my main game scene.
def game_scene():
    # Importing background image.
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Importing sprite image.
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Created a grid for the image background, that is 10x8 of the 16x16 images in it.
    background = stage.Grid(image_bank_background, 10, 8)

    # Creating a single sprite which will display the 5th image in the file (ship).
    # It will display 75 pixels to the right of the origin and 66 pixels down.
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Game variable which will display on the PyBadge and refresh it with 60 hertz.
    game = stage.Stage(ugame.display, 60)

    # Adding images to a list to display the first image in the pbm file.
    game.layers = [ship] + [background]

    # Adding the game variable to the game scene.
    game.render_block()

    # Using a while True loop to repeat my game forever until the user turns it off.

    while True:
        # Going to get user input.

        # Updating user game logic to proceed to the next step once the user carries out an action.
        # Redraw sprites to move the sprite around and not affect the background which will not change.
        game.render_sprites([ship])
        # Will wait until one 60th of a second has happened and then re-loop.
        # This will guarantee that we have a 60 second refresh rate for the background.
        game.tick()


if __name__ == "__main__":
    game_scene()
