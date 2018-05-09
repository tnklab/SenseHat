from sense_hat import SenseHat

## 3_1 tutorial

sense = SenseHat()
sense.show_message("Hello world ")

## 3_2 tutorial

r = 255
g = 255
b = 255
sense.clear((r,g,b)) ## White

## 3_6 & 3_7 tutorial
yellow = [255,255,0]
blue = [0,0,255]
while True:
    sense.show_message("Hello world",text_colour=yellow,back_colour=blue,scroll_speed=0.05)
    
