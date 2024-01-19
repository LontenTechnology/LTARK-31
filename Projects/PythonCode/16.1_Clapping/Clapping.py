from microbit import *

lightsOn = False

while True:
    if microphone.was_event(SoundEvent.LOUD):
        lightsOn = not lightsOn
        if lightsOn:
            display.show(Image.HEART)
        else:
            display.clear()
    sleep(100)
