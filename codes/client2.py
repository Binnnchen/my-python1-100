import socket
from threading import Thread
from json import dumps
from funtools import receive_all

addr = None
#客户端发送消息
def sending(client):
    while True:
        sendmsg = input()
        #3.客户端发送请求
        client.send(sendmsg.encode('utf-8'))
        if sendmsg == 'q':
            break
        #4.客户端接收来自服务器的消息
        
    #5.关闭客户端，释放资源
    client.close()
    """
    try: 
        client.close()
    except ConnectionAbortedError as e:
        print(e)
        print("通信已结束！")
    """

#客户端接收消息
def receive(client):
    while True:   
        #msg = client.recv(4096)        
        msg = receive_all(client) 

        if msg:       
            print(str(addr)+':'+msg.decode('utf-8'))

#客户端输入想要通信对象的地址
def connect_to():
    global addr
    host = input('请输入目的ip地址：')
    port = int(input('请输入目的端口号：'))
    addr = (host, port)
    return dumps(addr)

def main():
    #1.建立客户端socket对象
    #采用何种传输方式
    # 参数1：IPV4 参数2：TCP套接字
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind(('192.168.77.1', 7759))
    #2.设置目标服务器的IP地址，端口号，并与之建立连接
    host = '192.168.77.1'
    port = 1878
    client.connect((host, port))
    #to_ip, to_port = input('请输入您将要通信的对象的IP地址和端口号：')
    #to_addr.sendmsg
    #请求连接目的客户端
    to_addr = connect_to()
    client.send(to_addr.encode('utf-8'))

    #利用多线程进行客户端的接收与转发
    Thread(target=sending, args=(client, )).start()
    Thread(target=receive, args=(client, )).start()

if __name__ == '__main__':
    main()
    
