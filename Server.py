import socket

host = 'localhost'
port = 777
addr = (host, port)

sock = socket.socket()
sock.bind(addr)

sock.listen(2)
while True:
    conn, addr = sock.accept()
    print('client addr: ', addr)
    question = input('отправить значения ')
    if question != 'n':
        print(question)
        conn.send(byte(question))
    
sock.close()
