from sense_hat import SenseHat

hat = SenseHat()

while True:
    #加速度センサから加速度を取得
    acceleration = hat.get_accelerometer_raw()
    #取得した加速度を(x,y,z)に分ける
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    #加速度情報を小数点四捨五入する
    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)
    
    #加速度の画面表示
    print("x = %s[G], y = %s[G], z = %s[G]" % (x, y, z))
    