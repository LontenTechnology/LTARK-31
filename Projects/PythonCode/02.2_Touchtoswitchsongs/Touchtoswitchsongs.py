from microbit import *
import music
import random
while True:
    i = random.randint(0, 5)
    if pin_logo.is_touched():
        if i == 0:
            display.show(Image.TARGET)
            music.play(music.BA_DING)
        elif i == 1:
            display.show(Image.CHESSBOARD)
            music.play(music.CHASE)
        elif i == 2:
            display.show(Image.DIAMOND)
            music.play(music.DADADADUM)
        elif i == 3:
            display.show(Image.SQUARE)
            music.play(music.BADDY)
        elif i == 4:
            display.show(Image.SMALLSQUARE)
            music.play(music.FUNK)
        elif i == 5:
            display.show(Image.TRIANGLE)
            music.play(music.WEDDING)


