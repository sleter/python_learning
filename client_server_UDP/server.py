import socket
import time
import random

class manage_socket:
    host = '127.0.0.1' #local address
    port = 5678
    id = []
    id_pom = 1
    received_msg = ''
    number_of_tries = int((random.randrange(1, 8)+random.randrange(1, 8))/2)
    __secret_number = random.randrange(1, 10)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket family and type, Datagram -> UDP packet style
    s.bind((host, port))

    def addr_exists(self):
        if not manage_socket.id:
            return False
        for i in manage_socket.id:
            if(i[1]==str(manage_socket.addr)):
                return True
        return False


    def read_data(self):
        manage_socket.data, manage_socket.addr = manage_socket.s.recvfrom(1024) #grabbing data and address form socket, waiting for UDP packets
        manage_socket.read_time = time.ctime(time.time())
        manage_socket.received_msg = str(manage_socket.data.decode('utf-8'))
        if not(manage_socket.addr_exists(manage_socket.addr)):
            manage_socket.id.append([manage_socket.id_pom, str(manage_socket.addr)])
            manage_socket.id_pom+=1
        print(str(manage_socket.read_time)+":  "+str(manage_socket.data.decode('utf-8'))+'    '+manage_socket.id[manage_socket.id_pom-2][1])

    def send_data_id(self):
        for i in manage_socket.id:
            if(i[1]==str(manage_socket.addr)):
                str_pom = "ID: {}    INFO: {}".format(str(i[0]),i[1])
        print(str(manage_socket.read_time) + ":  " + str_pom )
        manage_socket.s.sendto(str_pom.encode('utf-8'),manage_socket.addr)

    def send_data_op(self):
            if(int(manage_socket.received_msg)==manage_socket.__secret_number):
                manage_socket.s.sendto(b'Zgadles!', manage_socket.addr)
            else:
                manage_socket.s.sendto(b'Nie zgadles!', manage_socket.addr)


def Main():
    m = manage_socket()
    print("Server Started.")
    while True:
        m.read_data()
        if(manage_socket.received_msg=='id'):
            m.send_data_id()
        elif(manage_socket.received_msg=='op'):
            str_pom = str(manage_socket.number_of_tries)
            m.s.sendto(str_pom.encode('utf-8'), m.addr)
            for i in range(m.number_of_tries):
                m.read_data()
                m.send_data_op()



    m.s.close()


if __name__ == '__main__':
    Main()
