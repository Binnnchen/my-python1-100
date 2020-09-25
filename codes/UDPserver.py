from socket import *

def main():
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    port = 12000
    serverSocket.bind(('', port))
    while True:
        message, clientaddr = serverSocket.recvfrom(2024)
        messa = message.decode('utf-8')
        if messa == 'q':
            break
        modifiedMessage = str(messa.count('de'))
        print(modifiedMessage)
        serverSocket.sendto(modifiedMessage.encode(), clientaddr)
    serverSocket.close()

if __name__ == "__main__":
    main()
