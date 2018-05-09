from sense_hat import SenseHat
import csv

hat = SenseHat()

while True:

    
    
    #気圧センサから気圧情報を取得
    pressure = hat.get_pressure()
    
    #小数点第１位で四捨五入する
    pressure = round(pressure, 1)
    
    #表示させる文字の列の生成
    msg = "Pressure=%s" % pressure

    #文字列の表示
    hat.show_message(msg,scroll_speed = 0.05)

    #ファイルを開く
    f = open('puressuredata.csv','a')

    csvWriter = csv.writer(f)

    #気圧センサから取得したデータをファイルに１行ずつ書き込む
    listdata = []
    listdata.append(pressure)
    print(listdata)
    csvWriter.writerow(listdata)

    f.close()#ファイルを閉じる
