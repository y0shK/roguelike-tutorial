# treat as engine.py

import pygame
import tcod as libtcod
from input_handlers import handle_keys

def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    libtcod.console_set_custom_font('roguelikeDev/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE) # no background for the @ player character
        libtcod.console_flush() # presents the background to the screen

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        # is the key press escape? if yes, user wants to quit the console, so quit the console
        if exit:
            return True

# are we running the program as a script or directory w/ python -m <program>.py?
if __name__ == '__main__':
    main()
