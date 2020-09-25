"""
提供客户端和服务器通用的方法
以供其直接调用
"""
#from abc import ABCMeta, abstractmethod
import sys

"""
接收完对方传输的所有数据，无论数据有多大
并返回接收到的字节流
"""

def receive_all(clientsocket):

    flag = True
    total_data = bytes()
    while flag:
        data = clientsocket.recv(1024)
        total_data += data 
        if sys.getsizeof(data) < 1024:
            flag = False
        else:
            next_data = clientsocket.recv(1024)
            total_data += next_data 
            if sys.getsizeof(next_data) < 1024:
                flag = False
    return total_data

"""
#这里本来是想利用子类继承父类的多态性来实现server与client的两个不同的接收消息方法
#后来发现想复杂了，根本不需要使用子类继承多态性
class obj_recv_all(object, metaclass=ABCMeta):
    def __init__(self, clientsocket):
        self.clientsocket = clientsocket
    
    def receive_all(self):
        #接收完对方传输的所有数据，无论数据有多大
        pass        

#服务器转发数据操作
class serv_recv_all(obj_recv_all):

    def receive_all(self):
        flag = True
        total_data = bytes()
        while flag:
            data = self.clientsocket.recv(1024)
            total_data += data 
            if sys.getsizeof(data) < 1024:
               flag = False
            else:
                next_data = self.clientsocket.recv(1024)
                total_data += next_data 
                if sys.getsizeof(next_data) < 1024:
                    flag = False
        return total_data 

#客户端接收数据
class clien_recv_all(obj_recv_all):

    def receive_all(self):
        flag = True
        total_data = bytes()
        while flag:
            data = self.clientsocket.recv(1024)
            total_data += data 
            if sys.getsizeof(data) < 1024:
               flag = False
            else:
                next_data = self.clientsocket.recv(1024)
                total_data += next_data 
                if sys.getsizeof(next_data) < 1024:
                    flag = False
        
               


#接收完对方传输的所有数据，无论数据有多大
def receive_all(clientsocket):
    flag = True
    total_data = bytes()
        
    while flag:
        data = clientsocket.recv(1024)
        total_data += data 
        if sys.getsizeof(data) < 1024:
            flag = False
        else:
            next_data = clientsocket.recv(1024)
            total_data += next_data 
            if sys.getsizeof(next_data) < 1024:
                flag = False
        msg = total_data.decode('utf-8')
        print("收到："+msg)
    """

