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
    dosya = open("text.txt", 'r')
    gonder = dosya.read()
    conn.send(gonder.encode("utf-8"))
    dosya.close()
    
s.close() #Socket isimiz bittiginden kapatiyoruz.
