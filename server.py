import socket


class transfer:
    host = socket.gethostname()

    def __init__(self):
        transfer.rand_tmp(self)

    def rand_tmp(self):
        s = socket.socket()
        port = 8080
        s.bind((self.host, port))
        s.listen(1)
        print('Waiting for connection to send rand_tm.txt...')
        conn, addr = s.accept()
        print(addr, 'has connected to server')
        file1 = open('rand_tmp.txt', 'rb')
        file_data1 = file1.read(999999)
        conn.send(file_data1)
        print('rand_tmp.txt has been sent!')
        transfer.fill_tmp(self)

    def fill_tmp(self):
        s = socket.socket()
        port = 8081
        s.bind((self.host, port))
        s.listen(1)
        print('Waiting for connection to send fill_tm.txt...')
        conn, addr = s.accept()
        print(addr, 'has connected to server')
        file2 = open('fill_tmp.txt', 'rb')
        file_data2 = file2.read(999999)
        conn.send(file_data2)
        print('fill_tmp has been sent!')

