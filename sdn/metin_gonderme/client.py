import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET IPv4 icin. SOCK_STREAM TCP protokolunde calisacagimizi belirtmek icin

port = 55555 #0-65535 portlara destek veriyor.Bizde cakismamasi icin yuksek deger verdik.
host = '10.0.0.1' #Mevcut tum arayuzler anlamina gelen semboli isim olmasi icin '' esitledik.

c.connect((host,port)) #Iki parantezin bir tuple tipi icin cunku bind tek arguman aliyor.
print("Baglantdi")

msg = c.recv(1024) #1024 alacagimiz limiti vermek icin yuksek bir rakamdir.MB veya GB degeri degildir.
print(msg.decode("utf-8")) #Mesaji cozebilmek icin decode yaptik.Decode parametresiz de calistirabiliriz utf-8 ekliyebiliriz.

c.close() #Islemler bittiginden dolayi socketi kapatiyoruz.
