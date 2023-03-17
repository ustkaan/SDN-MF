import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET IPv4 icin. SOCK_STREAM TCP protokolunde calisacagimizi belirtmek icin

port = 55555 #0-65535 portlara destek veriyor.Bizde cakismamasi icin yuksek deger verdik.
host = '10.0.0.1' #Mevcut tum arayuzler anlamina gelen semboli isim olmasi icin '' esitledik.

c.connect((host,port)) #Iki parantezin bir tuple tipi icin cunku bind tek arguman aliyor.
print("Baglanti saglandi")

dosya = open("text.txt", 'w')
metin = c.recv(1024)
dosya.write(metin.decode("utf-8"))
dosya.close()
    
c.close() #Islemler bittiginden dolayi socketi kapatiyoruz.
