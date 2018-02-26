from sense_hat import SenseHat

## 3_1 tutorial

sense = SenseHat()
sense.show_message("Hello world ")

## 3_2 tutorial

r = 255
g = 255
b = 255
sense.clear((r,g,b)) ## White

## 3_3 tutorial
blue = [0,0,255]
sense.show_message("Hello world ")


## 3_4 tutorial
animal = "cat"
score = 30
yellow = [255,255,0]
sense.show_message("Hello,world ", back_colour=[0,0,255],text_colour=yellow)


## 3_5 tutorial
sense.show_message("Hello,world ",text_colour=yellow,back_colour=blue)

## 3_6 & 3_7 tutorial

while True:
    sense.show_message("Hello world",text_colour=yellow,back_colour=blue,scroll_speed=0.05)
    
