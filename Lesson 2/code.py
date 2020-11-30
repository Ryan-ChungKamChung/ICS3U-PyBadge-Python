#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Setting background on the PyBadge

import ugame
import stage


def game_scene():
    # this function is the main game scene

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    while True:
        pass


if __name__ == "__main__":
    game_scene()
