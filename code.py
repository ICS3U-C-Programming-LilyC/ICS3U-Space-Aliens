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


# This function is for my menu game scene.
def menu_scene():
  # Importing background image.
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Adding the text objects.
    # Creating a list called text.
    text = []
    text1 = stage.Text(width = 29, height = 12, font = None, palette = constants.RED_PALLETTE, buffer = None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width = 29, height = 12, font = None, palette = constants.RED_PALLETTE, buffer = None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

  # Adding a grid background image that is 10x8.
    background = stage.Grid(image_bank_background, 10, 8)

  # Creating a stage for the background.
    game = stage.Stage(ugame.display, 60)
    game.layers = text + [background]

    game.render_block()
    
    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()
            
        game.tick()


def game_scene():
  # Importing background image.
      image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
      # Importing sprite image.
      image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

      # Buttons that will not change it's information/task.
      # When the game starts none of these buttons are being pressed (button_up).
      a_button = constants.button_state["button_up"]
      b_button = constants.button_state["button_up"]
      start_button = constants.button_state["button_up"]
      select_button = constants.button_state["button_up"]

      # Creating a sound variable that will take the sound from my pew.wav file and assign it to the sound variable.
      pew_sound = open("pew.wav", "rb")
      # To allow for the use of sound object (audio).
      sound = ugame.audio
      # Stopping the sound.
      sound.stop()
      # Not allowing for the sound to be muted.
      sound.mute(False)

      # Created a grid for the image background, that is 10x8 of the 16x16 images in it.
      background = stage.Grid(image_bank_background, 10, 8)

      # Creating a single sprite which will display the 5th image in the file (ship).
      # It will display 75 pixels to the right of the origin and 66 pixels down.
      ship = stage.Sprite(
          image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
      )

      # Creating another sprite which will display from the 9th image in the file (alien).
      # It will display in the middle of the screen and 16 pixles down from the top of the screen.
      alien = stage.Sprite(
          image_bank_sprites,
          9,
          int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
          16,
      )

      # Game variable which will display on the PyBadge and refresh it with 60 hertz.
      game = stage.Stage(ugame.display, 60)

      # Adding images to a list to display the first image in the pbm file.
      game.layers = [ship] + [alien] + [background]

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
              # Using and if statement for if the button is still being pressed then classify the button as in it's just released state.
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
              sound.play(pew_sound)

          # Redraw sprites to move the sprite around and not affect the background which will not change.
          game.render_sprites([ship] + [alien])
          # Will wait until one 60th of a second has happened and then re-loop.
          # This will guarantee that we have a 60 second refresh rate for the background.
          game.tick()

if __name__ == "__main__":
    menu_scene()