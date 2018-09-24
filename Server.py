import socket
from threading import Thread
import json

class socketServer(Thread):

    def __init__(self, addr):
        '''
        Коструктор
        :param addr: адресс сервера и порт для прослушки
        :param dictParameters: словарь со всеми параметрами принетые из формы
        '''
        self.addr = addr


    def run(self, dictParameters):

        self.dictParameters = dictParameters
        self.runPhotoscan()

    def runServer(self):
        self.sock = socket.socket()
        self.sock.bind(self.addr)
        self.sock.listen(2)

        self.connPhotoscan, addr = self.sock.accept()
        print('Фотоскан подключился: ', addr)
        #self.conArcGis, addr = sock.accept()
        #print('ArcGis подключен: ', addr)

    def sendMessage(self, conn, message):

        message = json.dumps(message)
        conn.send(bytes(message, encoding='utf-8'))

    def closeServer(self):
        self.sock.close()

    def runPhotoscan(self):
        '''
        Последовательность действий для фотоскана
        :return:
        '''
        self.sendMessage(self.connPhotoscan, self.dictParameters)
        while True:
            data = self.connPhotoscan.recv(1024)
            if data == b'vse':
                break
            print("data = ", data.decode('utf-8'))

    def runArcGis(self):
        pass

host = 'localhost'
port = 777
addr = (host, port)

dictParameters = dict()
dictParameters['ID_User'] = 'ID_1'


test = socketServer(addr)
test.runServer()
q = input()
#Отправляем команду на запуск с параметрами
test.run(dictParameters)

