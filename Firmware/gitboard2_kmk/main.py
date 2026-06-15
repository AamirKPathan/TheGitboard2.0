import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()

# -----------------------------
# PIN DEFINITIONS FOR XIAO
# -----------------------------
ROW_PINS = (board.D0, board.D1)
COL_PINS = (board.D2, board.D3, board.D4, board.D5)

# -----------------------------
# MATRIX SETUP (NO DIODES)
# -----------------------------
keyboard.matrix = MatrixScanner(
    row_pins=ROW_PINS,
    col_pins=COL_PINS,
    diode_orientation=DiodeOrientation.NONE,
)

# -----------------------------
# GITHUB MACROS (AUTO-TYPED)
# -----------------------------
GIT_ADD_ALL      = send_string("git add .")
GIT_COMMIT       = send_string('git commit -m ""')
GIT_PUSH         = send_string("git push")
GIT_PULL         = send_string("git pull")
GIT_NEW_BRANCH   = send_string("git checkout -b ")
GIT_SWITCH_BRANCH= send_string("git checkout ")
GIT_STATUS       = send_string("git status")
GIT_LOG          = send_string("git log")

# -----------------------------
# KEYMAP (8 keys)
# Row 0: K0  K1  K2  K3
# Row 1: K4  K5  K6  K7
#
# K0 = git add .
# K1 = git commit -m ""
# K2 = git push
# K3 = git pull
#
# K4 = git status
# K5 = git log
# K6 = git checkout -b (new branch)
# K7 = git checkout (switch branch)
# -----------------------------
keyboard.keymap = [
    [
        GIT_ADD_ALL,        # K0
        GIT_COMMIT,         # K1
        GIT_PUSH,           # K2
        GIT_PULL,           # K3

        GIT_STATUS,         # K4
        GIT_LOG,            # K5
        GIT_NEW_BRANCH,     # K6
        GIT_SWITCH_BRANCH,  # K7
    ]
]

if __name__ == '__main__':
    keyboard.go()
