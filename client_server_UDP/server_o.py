import socket
import random
import time
import re

class manage_socket:
    host = '127.0.0.1' #local address
    port = 5678 #random port > 1023
    #-----------------------------------------------------------------------------
    id = []
    id_pom = 1
    addr = ''
    addr_pom = []
    L = []
    number_of_tries = 0
    __secret_number = 0
    czy_ktos_zgadl = False
    bool_pom = False

    operacja = 0
    idd = ''
    czas = ''
    odpowiedz = ''
    final_packet = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket family and type, Datagram -> UDP packet style
    s.bind((host, port))

    def clear(self):
        self.operacja = 0
        self.idd = ''
        self.czas = ''
        self.odpowiedz = ''
        self.id.clear()
        self.id_pom = 1
        self.addr = ''
        self.addr_pom.clear()
        self.L.clear()
        self.number_of_tries = 0
        self.__secret_number = 0
        self.czy_ktos_zgadl = False

    def stworz_pakiet(self):
        self.final_packet = "Czas>"+self.czas+"<Identyfikator>"+self.idd+"<Operacja>"+str(self.operacja)+"<Odpowiedz>"+self.odpowiedz+"<"

    def decode_packet(self):
        data, self.addr = self.s.recvfrom(1024)
        data = data.decode('utf-8')
        result = re.findall('>(.*?)<', data)
        self.czas = result[0]
        self.idd = result[1]
        self.operacja = int(result[2])
        self.odpowiedz = result[3]
        self.stworz_pakiet()
        print('Odebrano: '+self.final_packet)


    def send_packet(self):
        self.czas = time.ctime(time.time())
        self.stworz_pakiet()
        self.s.sendto(self.final_packet.encode('utf-8'), self.addr)  # send to server
        print('Wysłano: '+self.final_packet)


    def give_id(self):
        self.decode_packet()#grabbing data and address form socket, waiting for UDP packets
        self.id.append(str(self.id_pom))
        self.addr_pom.append(self.addr)
        self.idd = self.id[self.id_pom-1]
        self.id_pom += 1
        self.send_packet()

    def getL(self):
        if(self.addr_pom == ''):
            self.addr_pom = self.addr
        self.decode_packet()
        self.L.append(self.operacja)

    def give_number_of_tries(self):
        self.__secret_number = random.randrange(1, 10)
        self.number_of_tries = int((self.L[0] + self.L[1]) / 2)
        self.operacja = self.number_of_tries
        self.addr = self.addr_pom[0]
        self.idd = "1"
        self.send_packet()
        self.addr = self.addr_pom[1]
        self.idd = "2"
        self.send_packet()

    def check_number(self):
        self.decode_packet()
        if not(self.czy_ktos_zgadl):
            if(int(self.odpowiedz) == self.__secret_number):
                self.odpowiedz = 'Zgadłeś!'
                self.czy_ktos_zgadl = True
            else:
                self.odpowiedz = 'Nie zgadłeś!'
        else:
            self.odpowiedz = "Przeciwnik zgadł pierwszy!"
        self.send_packet()




def Main():
    print("Server started")
    m = manage_socket()
    while True:
        m.bool_pom = False
        m.give_id()
        m.give_id()
        m.getL()
        m.getL()
        m.give_number_of_tries()
        while True:
            m.check_number()
            if(m.bool_pom):
                m.clear()
                print("Server rebooted")
                break
            if(m.czy_ktos_zgadl):
                m.bool_pom = True

if __name__ == '__main__':
    Main()
