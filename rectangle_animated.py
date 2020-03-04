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
O = (0, 0, 0)

colors = [G, Y, B, R, W, P]

def square_1():
    C = random.choice(colors)
    logo = [
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,C,C,O,O,O,
    O,O,O,C,C,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    ]
    return logo
def square_2():
    C = random.choice(colors)
    logo = [
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    O,O,C,C,C,C,O,O,
    O,O,C,O,O,C,O,O,
    O,O,C,O,O,C,O,O,
    O,O,C,C,C,C,O,O,
    O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O,
    ]
    return logo
def square_3():
    C = random.choice(colors)
    logo = [
    O,O,O,O,O,O,O,O,
    O,C,C,C,C,C,C,O,
    O,C,O,O,O,O,C,O,
    O,C,O,O,O,O,C,O,
    O,C,O,O,O,O,C,O,
    O,C,O,O,O,O,C,O,
    O,C,C,C,C,C,C,O,
    O,O,O,O,O,O,O,O,
    ]
    return logo
def square_4():
    C = random.choice(colors)
    logo = [
    C,C,C,C,C,C,C,C,
    C,O,O,O,O,O,O,C,
    C,O,O,O,O,O,O,C,
    C,O,O,O,O,O,O,C,
    C,O,O,O,O,O,O,C,
    C,O,O,O,O,O,O,C,
    C,O,O,O,O,O,O,C,
    C,C,C,C,C,C,C,C,
    ]
    return logo

squares = [square_1, square_2, square_3, square_4]
count = 0
s.clear()

while True:
  s.set_pixels(squares[count % len(squares)]())
  count += 1
  time.sleep(1)