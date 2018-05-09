from sense_hat import SenseHat

hat = SenseHat()

while True:
    #気圧センサから情報を取得する
    pres = hat.get_pressure()
    #小数第１位で四捨五入させる
    pres = round(pres, 1)
    
    #表示させる文字列の生成
    msg = "Pressure = %s[hPa]" % pres
    
    #文字列の表示
    hat.show_message(msg, scroll_speed = 0.05)