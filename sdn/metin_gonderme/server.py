import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET IPv4 icin. SOCK_STREAM TCP protokolunde calisacagimizi belirtmek icin

port = 55555 #0-65535 portlara destek veriyor.Bizde cakismamasi icin yuksek deger verdik.
host = '10.0.0.1' #Mevcut tum arayuzler anlamina gelen semboli isim olmasi icin '' esitledik.
    
s.bind((host,port)) #Socketi adrese baglamak icin
s.listen() #Server max kac kisinin baglanacagini belirtmek icin.Bos birakilir ise sonsuz olur.
#Server max kac kisinin baglanacagini belirtmek icin deger girilmelidir.Bos birakilir ise sonsuz olur.
conn, adress = s.accept()  #Baglanti kurulmasi icin
print(adress)
if conn: #Baglanti saglandigi kontrolunu yapmak icin
    conn.send("Bu text mesaj".encode("utf-8")) #Stringi gondermek icin encode etmemiz lazim yoksa string direkt gonderilemiyor socket uzerinden.
    #utf-8 Turkce karakterler desteklemesi icin
    
s.close() #Socket isimiz bittiginden kapatiyoruz.
