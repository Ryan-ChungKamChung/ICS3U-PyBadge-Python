#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Setting background on the PyBadge


import ugame
import stage

import constants


def game_scene():
    # this function is the main game scene

    # image bank
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # set background to img 0 and 10x8 tiles of size 16x16
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, 
                            constants.SCREEN_GRID_Y)

    # sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # creates stage and sets it to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    
    # sets the layers of all sprites, in order
    game.layers = [ship] + [background]
    
    # renders all sprites, only once
    game.render_block()

    # forever game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
    
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass 
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        # update game logic
        
        #redraw Sprite
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
