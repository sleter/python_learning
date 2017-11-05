import socket

def Main():
    host = '127.0.0.1'
    port = 15200 #random not used port

    server = ('127.0.0.1',5678) #localhost + server port

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind((host, port))
    except:
        port +=1
        s.bind((host, port))

    message = ''
    while message != 'quit':
        message = input("> ")
        if(message=='op'):
            s.sendto(message.encode('utf-8'), server)  # send to server
            data, addr = s.recvfrom(1024)
            print('Masz '+data.decode('utf-8')+' szanse')
            number_of_tries = str(data.decode('utf-8'))
            number_of_tries = int(number_of_tries)
            for i in range(0,number_of_tries):
                if(data.decode('utf-8')=='Zgadles!'): break
                message = input("Operacja> ")
                s.sendto(message.encode('utf-8'), server) #send to server
                try:
                    data, addr = s.recvfrom(1024) #receive data from server
                    print(data.decode('utf-8'))
                except:
                    print("server not working")
                    break
            print('Koniec prób')
        elif(message=='id'):
            s.sendto(message.encode('utf-8'), server) #send to server
            try:
                data, addr = s.recvfrom(1024) #receive data from server
                print('Identyfikator> ' + data.decode('utf-8'))
            except:
                print("server not working")
                break

    s.close()

if __name__ == '__main__':
    Main()
