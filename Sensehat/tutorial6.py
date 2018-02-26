from sense_hat import SenseHat

sense = SenseHat()

red = (255,0,0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
# 絶対値
    x = abs(x)
    y = abs(y)
    z = abs(z)
# 加速度を図っている。１以上であれば！がリアルタイムでみれる。
    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!",red)
    else:
        sense.clear()

