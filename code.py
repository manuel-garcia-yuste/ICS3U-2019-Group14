#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : January 2020
# Final proyect

import random
import ugame
import stage

import constants

# image bank
image_bank_1 = stage.Bank.from_bmp16("paddle5.bmp")
# a list of sprites that will be updated every frame

# get sound ready
pew_sound = open("pong_sound.wav", 'rb')
sound = ugame.audio
sound.stop()
sound.mute(False)


def menu():
    background = stage.Grid(image_bank_1, 10, 8)

    text = []
    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(55, 50)
    text1.text("WELCOME!")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(40, 70)
    text2.text("PRESS START")
    text.append(text2)

    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()



def game_scene():
    # this function is a scene
    sprites = []

    ball_direction_x = 1
    ball_direction_y = 1

    # sets the paddle
    background = stage.Grid(image_bank_1, 10, 8)

    # parameters (image_bank, image # in bank, x, y)
    paddle = stage.Sprite(image_bank_1, 5, 140, 56)
    sprites.insert(0, paddle)

    # parameters (image_bank, image # in bank, x, y)
    paddle2 = stage.Sprite(image_bank_1, 5, 5, 56)
    sprites.insert(0, paddle2)

    # parameters (image_bank, image # in bank, x, y)
    ball = stage.Sprite(image_bank_1, 6, 50, 56)
    sprites.insert(0, ball)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
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
        if keys & ugame.K_UP:
            if paddle.y > 0:
                paddle.move(paddle.x, paddle.y - 1)
            pass
        if keys & ugame.K_DOWN:
            if paddle.y < constants.SCREEN_Y - constants.SPRITE_SIZE:
                paddle.move(paddle.x, paddle.y + 1)
            pass

        # update game logic
        if stage.collide(paddle.x + 7, paddle.y, paddle.x + 9, paddle.y + 16,
                             ball.x + 4, ball.y + 4, ball.x + 8, ball.y + 8):
            ball_direction_x = -1
            ball_direction_y = -1
            sound.stop()
            sound.play(pew_sound)
        else:
            # ball.move(ball.x + constants.SPRITE_MOVEMENT_SPEED, ball.y)
            pass

            # update game logic
        if stage.collide(paddle2.x + 7, paddle2.y, paddle2.x + 9, paddle2.y + 16,
                             ball.x + 4, ball.y + 4, ball.x + 8, ball.y + 8):
            ball_direction_x = 1
            ball_direction_y = 1
            sound.stop()
            sound.play(pew_sound)
        else:
            # ball.move(ball.x + constants.SPRITE_MOVEMENT_SPEED, ball.y)
            pass

        if ball.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
            ball_direction_x = 1
            ball_direction_y = -1

        if ball.y < 0:
            ball_direction_x = -1
            ball_direction_y = 1

        if ball.y > 0:
            paddle2.move(paddle2.x, ball.y)

        ball.move(ball.x + ball_direction_x, ball.y + ball_direction_y)
        if ball.x > 140:
            game_over()

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


def game_over():
    background = stage.Grid(image_bank_1, 10, 8)

    text = []
    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(50, 10)
    text1.text("GAME OVER")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            menu()


if __name__ == "__main__":
    menu()
