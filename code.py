#!/usr/bin/env python3

# Created by: Lily Carroll
# This program is the "Dino Blaster" program on the PyBadge.
# Importing Circuit Python libraries.
#!/usr/bin/env python3

# Created by: Lily Carroll
# This program is the "Dino Blaster" program on the PyBadge.
# Importing Circuit Python libraries.
import stage
import ugame

import constants


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
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # Game variable which will display on the PyBadge and refresh it with 60 hertz.
    game = stage.Stage(ugame.display, 60)

    # Adding images to a list to display the first image in the pbm file.
    game.layers = [ship] + [background]

    # Adding the game variable to the game scene.
    game.render_block()

    # Using a while True loop to repeat my game forever until the user turns it off.

    while True:
        # Going to get user input.
        # Figuring out what buttons are being pressed on the PyBadge.
        keys = ugame.buttons.get_pressed()

        # If the A button is being pressed then it returns "A".
        if keys & ugame.K_X:
            pass

        # If the B button is being pressed then it returns "B".
        if keys & ugame.K_O:
            pass

        # If the START button is being pressed then it returns "Start".
        if keys & ugame.K_START:
            pass

        # If the SELECT button is being pressed then it returns "Select".
        if keys & ugame.K_SELECT:
            pass
        # If the right button is being pressed then it moves the ship right (by 1 pixel) from its current position along the x direction.
        if keys & ugame.K_RIGHT:
            # Using an if statement to check if the ship's position is less than or equal to 160 pixels then we can move the ship over.
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
                # Otherwise set it to 0 to keep the ship from moving off the screen.
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        # If the left button is being pressed then it moves the ship left (by 1 pixel) from its current position along the y direction.
        if keys & ugame.K_LEFT:
            # Using an if statement to allow the ship to go right up to the edge of the Pybadge screen.
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            # Otherwise set it to 0 to keep the ship from moving off the screen.
            else:
                ship.move(0, ship.y)

        # If the up button is being pressed it moves the ship up (by 1 pixel) by decreasing the y direction.
        if keys & ugame.K_UP:
            pass

        # If the down button is being pressed it moves the ship down (by 1 pixel) by increasing the y direction.
        if keys & ugame.K_DOWN:
            pass

        # Updating user game logic to proceed to the next step once the user carries out an action.
        # Redraw sprites to move the sprite around and not affect the background which will not change.
        game.render_sprites([ship])
        # Will wait until one 60th of a second has happened and then re-loop.
        # This will guarantee that we have a 60 second refresh rate for the background.
        game.tick()


if __name__ == "__main__":
    game_scene()
