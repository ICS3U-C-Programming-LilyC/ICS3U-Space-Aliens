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

    # Created a grid for the image background, that is 10x8 of the 16x16 images in it.
    background = stage.Grid(image_bank_background, 10, 8)

    # Game variable which will display on the PyBadge and refreshing it with 60 Hertez
    game = stage.Stage(ugame.display, 60)

    # Adding images to a list to display the first image in the pbm file.
    game.layers = [background]

    # Adding the game variable to the game scene.
    game.render_block()

    # Using a while true loop to repeat my game forever until user turns it off.

    while True:
        pass  # Using as a placeholder

if __name__ == "__main__":
    game_scene()
