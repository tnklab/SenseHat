from sense_hat import SenseHat
sense = SenseHat()

def red():
    sense.clear(255,0,0)

def blue():
    sense.clear(0,0,255)

def green():
    sense.clear(0,255,0)

def yellow():
    sense.clear(255,255,0)
# 上下右左で色が変わったりする。真ん中で色が消える。
sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear

while True:
    pass
