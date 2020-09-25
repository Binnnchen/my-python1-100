from socket import *

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    host = '192.168.77.1'
    port = 11991
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    print("服务器已启动监听！")
    connectingSocket, clientaddr = serverSocket.accept()
    print("已与客户%s建立连接！" % str(clientaddr))
    while True:
        message = connectingSocket.recv(2048).decode('utf-8')
        modifiedMessage = message.upper()
        print(modifiedMessage)
        connectingSocket.send(modifiedMessage.encode('utf-8'))
    connectingSocket.close()

if __name__ == "__main__":
    main()