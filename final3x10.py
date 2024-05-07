# 3x10 keyboard with two holes in the matrix at positions 11 and 29
# Author: Megan Huang <mhuang25@amherst.edu>
# Last Modified: 7 May 2024

# Notes: 
# file name "code.py" within directory.
# adapted from John Park: https://learn.adafruit.com/numpad-4000-mechanical-keyswitch-data-entry-device/code-and-use-the-numpad-4000
# requires the python 9 library contents from the guide's project bundle


import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

COLUMNS = 3
ROWS = 10

# designate pins on the KB2040 
keys = keypad.KeyMatrix(
    column_pins=(board.A0, board.A1, board.A2),  # row pins
    row_pins=(board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9),  # column pins
    columns_to_anodes=False,
)
kbd = Keyboard(usb_hid.devices)

#  0   1   2   3   4   5   6   7   8   9
# 10  11  12  13  14  15  16  17  18  19
# 20  21  22  __  23  24  25  26  27  __

# maps to alphabet, spacebar, and backspace
keymap = {
            0: Keycode.A,
            1: Keycode.B,
            2: Keycode.C,
            3: Keycode.D,
            4: Keycode.E,
            5: Keycode.F,
            6: Keycode.G,
            7: Keycode.H,
            8: Keycode.I,
            9: Keycode.J,

            10: Keycode.K,
            #11: Keycode.L, # hole skipped
            12: Keycode.L,
            13: Keycode.M,
            14: Keycode.N,
            15: Keycode.O,
            16: Keycode.P,
            17: Keycode.Q,
            18: Keycode.R,
            19: Keycode.S,
            20: Keycode.T,
            21: Keycode.U,
            22: Keycode.V,
            23: Keycode.W,
            24: Keycode.X,
            25: Keycode.Y,
            26: Keycode.Z,
            27: Keycode.SPACEBAR,
            28: Keycode.BACKSPACE,

}

# test:
#abcdefghijklmnopqruurtrstuvwxyz

# handle key presses without lights
while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event.key_number) # debug output
        if key_event.pressed:
            kbd.press(keymap[key_event.key_number])
        if key_event.released:
            kbd.release(keymap[key_event.key_number])