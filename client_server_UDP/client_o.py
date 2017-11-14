import socket
import time
import re
import random

class packet:
    host = '127.0.0.1'
    port = random.randrange(5000,20000) #random not used port

    server = ('127.0.0.1', 5678) #localhost + server port

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind((host, port))
    except:
        port +=1
        s.bind((host, port))

    L = 0
    max = 0
    czy_ktos_zgadl = False
    #-------------------------------------------------------
    operacja = 0
    czas = ''
    id = ''
    odpowiedz = ''
    final_packet = ''

    #-------------------------------------------------------
    def stworz_pakiet(self):
        self.final_packet = "Czas>"+self.czas+"<Identyfikator>"+self.id+"<Operacja>"+str(self.operacja)+"<Odpowiedz>"+self.odpowiedz+"<"

    def decode_packet(self):
        data, addr = self.s.recvfrom(1024)
        data = data.decode('utf-8')
        result = re.findall('>(.*?)<', data)
        self.czas = result[0]
        self.id = result[1]
        self.operacja = int(result[2])
        self.odpowiedz = result[3]
        self.stworz_pakiet()
        print('Odebrano: '+self.final_packet)


    def send_packet(self):
        self.czas = time.ctime(time.time())
        self.stworz_pakiet()
        self.s.sendto(self.final_packet.encode('utf-8'), self.server)  # send to server
        print('Wysłano: '+self.final_packet)

    def proceed(self):
        self.send_packet()
        self.decode_packet()

    def proceed1(self):
        self.L = input("Podaj L: ")
        self.operacja = self.L
        self.send_packet()
        self.decode_packet()
        self.max = self.operacja
        print("Masz {} prób/y \n Wylosowana liczb jest z przedziału <1;9>".format(self.operacja))

    def guess(self):
        self.odpowiedz = input("Zgadnij liczbe: ")
        self.proceed()
        print(self.odpowiedz)
        if(self.odpowiedz == 'Zgadłeś!'):
            self.max = 0
        elif(self.odpowiedz == "Przeciwnik zgadł pierwszy!"):
            self.czy_ktos_zgadl = True

def Main():
    p = packet()
    p.proceed()
    p.proceed1()
    while p.max != 0:
        if(p.czy_ktos_zgadl):
            break;
        p.max -= 1
        p.guess()



if __name__ == '__main__':
    Main()