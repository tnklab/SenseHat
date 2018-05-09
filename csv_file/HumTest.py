from sense_hat import SenseHat
import csv

hat = SenseHat()

while True:
    #湿度センサから湿度情報を取得する
    hum = hat.get_humidity()
    #小数第１位で四捨五入させる
    hum = round(hum, 1)
    
    #表示させる文字列の生成
    msg = "Humidity = %s" % hum
    
    #文字列の表示
    hat.show_message(msg, scroll_speed = 0.05)

    f = open('humiditydata.csv','a')#ファイルを開く　

    csvWriter = csv.writer(f)

    #湿度センサから取得したデータをファイルに１行ずつ書き込む
    listdata = []
    listdata.append(hum)
    print(listdata)
    csvWriter.writerow(listdata)

    f.close()#ファイルを閉じる
