from sense_hat import SenseHat

from random import randint
sense = SenseHat()

while True:
    colour = (0,0,0)
    randomBackgroundCol = (randint(0,255),randint(0,255),randint(0,255))
    sense.show_message("Hello! We are New Media Development :)", text_colour= colour,back_colour=randomBackgroundCol)
    sense.low_light = True