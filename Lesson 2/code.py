#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# "Hello, World!" on a PyBadge


import ugame
import stage


def game_scene():
    # main game scene
    
    # image bank
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    
    # sets bg to tile 0 of the image bank
    # 10x8 tiles of 16x16 pixels
    background = stage.Grid(image_bank_background, 10, 8)
    
    # creates game stage for bg and sets it to 60fps
    game = stage.Stage(ugame.display, 60)
    # sets layers of sprites, items show in orger
    game_layers = [background]
    # renders bg, most likely only once per scene
    game.render_block()

    # repeats forever, game loop
    while True:
        pass


if __name__ == "__main__":
    game_scene()
