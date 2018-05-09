from sense_hat import SenseHat
import csv

hat = SenseHat()

while True:

    
    
    #温度センサから温度情報を取得
    temperature = hat.get_temperature()
    
    #小数点第１位で四捨五入する
    temperature = round(temperature, 1)
    
    #表示させる文字の列の生成
    msg = "temperature=%s" % temperature

    #文字列の表示
    hat.show_message(msg,scroll_speed = 0.05)

    #ファイルを開く
    f = open('temperaturedata.csv','a')

    csvWriter = csv.writer(f)

    #温度センサから取得したデータをファイルに１行ずつ書き込む
    listdata = []
    listdata.append(temperature)
    print(listdata)
    csvWriter.writerow(listdata)

    f.close()#ファイルを閉じる
