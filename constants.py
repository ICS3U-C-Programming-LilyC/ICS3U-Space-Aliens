#!/usr/bin/env python3

# Created by: Lily Carroll
# This file holds my constants.

# Pybadge screen size is 160x128 and sprites are 16x16.
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# Creating a dictionary to keep track of when the buttons were last pressed, since we want to be able to shoot 60 missiles in 60 seconds.
# This allows for the button to be pressed and released quicker to achieve this timing for 60 missiles in 60 seconds.
button_state = {
    "button_up": "up",
    "button_just_pressed": "just_pressed",
    "button_still_pressed": "still_pressed",
    "button_released": "released",
}

# Creating a red pallet to display the text in red on the PyBadge.
RED_PALLETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
