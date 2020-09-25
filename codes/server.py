from socket import socket
from json import dumps
from base64 import b64encode
from threading import Thread

def main():

    class FileTransferhandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient
        
        def run(self):
            my_dict = {}
            my_dict['filename'] = 'xixi.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()
        
    server = socket()
    server.bind(('192.168.77.1', 7796))
    server.listen(512)
    print('服务器启动开始监听...')
    with open(r'e:\美女图片\xixi.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferhandler(client).start()

if __name__ == '__main__':
    main()