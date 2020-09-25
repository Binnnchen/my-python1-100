import socket
from threading import Thread
from json import loads
from funtools import receive_all

#服务器记录上线的客户及对应的连接关系
clients={}
client_to_client={}
"""
client_to_client={('192.168.77.1', 7756):('192.168.77.1', 7759),
                ('192.168.77.1', 7759):('192.168.77.1', 7756)
                }
"""

#根据客户端的addr找到其socket对象
def find_key(addr, clients):
    return [key for key, value in clients.items() if value == addr][0]

#记录已连接上的客户端
"""
class wait_accept(Thread):

    def __init__(self, server):
        super().__init__()
        self.server = server
        #self.addr = None
        #self.clientsocket = None
    
    def run(self):
        #4.等待客户端的连接
        #accept()方法返回一个元组
        #元素1：客户端的socket对象（即服务器与客户端沟通的媒介） 
        #元素2：客户端地址，也是元组，（Ipv4， port）
        while True:
            self.clientsocket, self.addr = self.server.accept()
            clients[self.clientsocket] = self.addr
            print(str(self.addr)+"上线了！")
"""
#查看目标是否在线，有则开始通信
class find_connecting(Thread):
    def __init__(self, server, clientsocket, addr):
        super().__init__()
        self.server = server
        self.clientsocket = clientsocket
        self.addr = addr
    
    def run(self):
        to_addr_data = self.clientsocket.recv(1024).decode('utf-8')
        to_addr = tuple(loads(to_addr_data))
        #print(to_addr)
        
        if to_addr in clients.values():
            print("用户"+str(to_addr)+"在线!")
            source = self.addr
            des = to_addr
            client_to_client[source] = des
            client_to_client[des] = source
            #服务器转发数据
            message_handler(self.server, self.clientsocket, self.addr).start()
        else:
            print("用户"+str(to_addr)+"不在线！")
            


#定义一个服务器转发处理多线程类
class message_handler(Thread):

    def __init__(self, server, clientsocket, addr):
        super().__init__()
        self.server = server
        self.clientsocket = clientsocket
        self.addr = addr
    
    def run(self):
        while True: 
            
            #msg = self.clientsocket.recv(4096)
            msg = receive_all(self.clientsocket)
            if msg:
                to_addr = client_to_client[self.addr]
                to_clientsocket = find_key(to_addr, clients)
                to_clientsocket.send(msg)


def main():
    #1.创建服务器的socket对象
    #并指定何种传输方式，
    # socket.AF_INET : IPV4, socket.SOCK_STREAM : TCP套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.绑定服务器地址ip,端口号
    #注意传入的参数是一个元组对象
    host = '192.168.77.1'
    port = 1878
    server.bind((host, port))
    #3.设置监听器，最大连接的客户端数
    server.listen(6)
    
    while True:

        #记录已连接的客户端
        
        clientsocket, addr = server.accept()
        clients[clientsocket] = addr
        print(str(addr)+"上线了！")
        
        find_connecting(server, clientsocket, addr).start()
        
        #服务器转发数据
        #message_handler(server, clientsocket, addr).start()
        #6.传输数据给客户端
        #msg = input('回复：')
        #clientsocket.send(msg.encode('utf-8'))
    #7.关闭服务器socket对象，释放资源
    server.close()

if __name__ == '__main__':
    main()
        