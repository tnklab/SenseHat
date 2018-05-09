from sense_hat import SenseHat

hat = SenseHat()

while True:
    #湿度センサから情報を取得する
    hum = hat.get_humidity()
    #小数第１位で四捨五入させる
    hum = round(hum, 1)
    
    #表示させる文字列の生成
    msg = "Humidity = %s" % hum
    
    #文字列の表示
    hat.show_message(msg, scroll_speed = 0.05)