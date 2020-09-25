from socket import *

def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    serverhost = "192.168.77.1"
    serverport = 11991
    clientSocket.connect((serverhost, serverport))
    while True:
        message = input("请输入：")
        if message == 'q':
            break
        clientSocket.send(message.encode('utf-8'))
        data = clientSocket.recv(2048)
        if data:
            modifiedMessage = data.decode('utf-8')    
            print(modifiedMessage)
    clientSocket.close()

if __name__ == "__main__":
    main()