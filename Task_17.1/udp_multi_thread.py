import socket
import threading

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    serverIP = "192.168.163.154"
    serverPort = 1234
    while True:
        msg = input().encode()
        # sending the packet
        sock.sendto(msg, (serverIP, serverPort))

def server():
    import socket

    # using UDP protocol for connection
    # SOCK_DGRAM for UDP and AF_INET for using IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #  IP of server(linux machine)
    ip = "192.168.163.126"
    port = 1235

    # binding the port and IP to the socket
    sock.bind((ip, port))

    # receiving packet from the client or another server
    # parameter in recvfrom(20) is  size of the packet
    while True:
        msg = sock.recvfrom(20)
        print(msg[1][0], end = ": ")
        print(msg[0].decode())

if __name__ == "__main__":
    p1 = threading.Thread(target=client)
    p2 = threading.Thread(target=server)
    p1.start()
    p2.start()

