from sense_hat import SenseHat

hat = SenseHat()

while True:
    #温度センサから情報を取得する
    tmp = hat.get_temperature()
    #小数第１位で四捨五入させる
    tmp = round(tmp, 1)
    
    #表示させる文字列の生成
    msg = "Temperature = %s" % tmp
    
    #文字列の表示
    hat.show_message(msg, scroll_speed = 0.05)