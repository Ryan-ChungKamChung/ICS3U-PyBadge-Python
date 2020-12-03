#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Setting background on the PyBadge


import ugame
import stage


def game_scene():
    # this function is the main game scene
    
    # image bank
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # set background to img 0 and 10x8 tiles of size 16x16
    background = stage.Grid(image_bank_background, 10, 8)

    # sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # creates stage and sets it to 60fps
    game = stage.Stage(ugame.display, 60)
    
    # sets the layers of all sprites, in order
    game.layers = [ship] + [background]
    
    # renders all sprites, only once
    game.render_block()

    # forever game loop
    while True:
        # get user input
        
        # update game logic
        
        #redraw Sprite
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
