import socket
import threading

class server:
    def __init__(self):
        self.SERVER = "192.168.163.126"
        print(self.SERVER)
        self.PORT = 1234
        self.ADDR = (self.SERVER, self.PORT)
        self.HEADER = 64
        self.FORMAT = 'utf-8'
        self.DISCONNECT = "diconnect"

        # setting the connection as STREAM i.e. TCP connection
        # binding the ports
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # making the port reusable
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.bind(self.ADDR)
        
        # listing to the port
        self.server.listen()

    def send_msg(self, conn, addr):
        while True:
            self.msg = input()
            self.message = self.msg.encode(self.FORMAT)
            self.msg_length = len(self.message)
            self.send_length = str(self.msg_length).encode(self.FORMAT)
            self.send_length += b' ' * (self.HEADER - len(self.send_length))
            self.conn.send(self.send_length)
            self.conn.send(self.message)

    def recv_msg(self, conn, addr):
        # receiving the message length first for the header of the message
        # in case the message is too long or too short.
        self.connected = True
        while self.connected:
            self.msg_length = self.conn.recv(self.HEADER).decode(self.FORMAT)
            if self.msg_length:
                self.msg_length = int(self.msg_length)

                # receiving message of the full length  
                self.msg = self.conn.recv(self.msg_length).decode(self.FORMAT)
                if self.msg == self.DISCONNECT:
                    self.connection = False
                if self.msg != "":
                    print(f"[{self.addr[0]}] {self.msg}")
        self.conn.close()

    # handling the clients after connection is accepted
    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {self.addr}")
        # creating thread for sending and receiving msg
        # it will enable us to send and recieve messages simultaneously
        self.send_thread = threading.Thread(target=self.send_msg, args=(self.conn, self.addr))
        self.recv_thread = threading.Thread(target=self.recv_msg,args=(self.conn, self.addr))
        self.send_thread.start()
        self.recv_thread.start()


    # starting the server
    def start(self):
        while True:
            # accepting the clients   
            self.conn, self.addr = self.server.accept()
            self.thread = threading.Thread(target=self.handle_client, args=(self.conn, self.addr))
            self.thread.start()
            # printing active connections
            print("[ACTIVE CONNECTION] ", {threading.activeCount()-2})


print("[SERVER STARTING...]")
obj = server()
start_server = threading.Thread(target=obj.start)
start_server.start()    