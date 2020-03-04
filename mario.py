from sense_hat import SenseHat
import time
import random

s = SenseHat()

R = (172,5,40)
H = (250,159,73)
B = (0,0,196)
O = (0, 0, 0)

mario = [
O,O,R,R,R,O,O,O,
O,O,R,R,R,R,R,O,
O,O,H,O,H,O,O,O,
O,O,H,H,O,H,O,O,
O,B,B,R,B,R,O,O,
B,O,B,H,R,H,B,O,
O,O,R,R,R,R,O,O,
O,O,B,O,O,B,O,O,
]

mario_jump = [
O,O,O,R,R,R,O,O,
O,R,R,R,R,R,O,O,
O,O,O,H,O,H,O,O,
B,O,H,O,H,H,O,B,
O,B,B,R,B,R,B,O,
O,O,B,H,R,H,O,O,
O,B,R,R,R,R,B,O,
O,O,O,O,O,O,O,O,
]

while True:
  s.set_pixels(mario)
  time.sleep(1)
  s.set_pixels(mario_jump)
  time.sleep(1)
  