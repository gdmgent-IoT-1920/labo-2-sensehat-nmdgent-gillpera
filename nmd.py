
from sense_hat import SenseHat
import time
import random

s = SenseHat()

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
P = (255,105, 180)

colors = [G, Y, B, R, W, P]
displayString = input("geef woord in")
speed = float(input('gewenste snelheid'))

while True: 
  for letter in displayString:
    s.show_letter(letter, random.choice(colors))
    time.sleep(speed)
  time.sleep(3)