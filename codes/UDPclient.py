"""
UDP是无连接的协议，不需建立连接，直接朝着目的地址把报文发过去
"""
from socket import *

def main():
    #创建客户端套接字对象
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    serverhost = "192.168.77.1"
    serverport = 12000
    while True:
        message = input("请输入一段连续字母：")
        clientSocket.sendto(message.encode('utf-8'), (serverhost, serverport))
        if message == 'q':
            break
        modifiedMessage, serveraddr = clientSocket.recvfrom(2024)
        print(modifiedMessage.decode('utf-8'))
    clientSocket.close()

if __name__ == '__main__':
    main()




