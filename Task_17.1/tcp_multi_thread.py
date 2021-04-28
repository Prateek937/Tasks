import socket
import threading

class server:
    def __init__(self):
        self.SERVER = '192.168.8.126'
        self.PORT = 1237
        self.ADDR = (self.SERVER, self.PORT)
        self.HEADER = 64
        self.FORMAT = 'utf-8'
        self.DISCONNECT = "diconnect"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
            
    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION {self.addr} connected.")

        self.connected = True
        while self.connected:
            self.msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if self.msg_length:
                self.msg_length = int(self.msg_length)
                self.msg = self.conn.recv(self.msg_length).decode(self.FORMAT)
                if self.msg == self.DISCONNECT:
                    self.connected = False
                print(f"{self.addr}: {self.msg}")
        
        self.conn.close()

    def start_server(self):
        print("[STARTING] Getting ready to connect...")
        print("[STARTED] Chat program ready.")
        
        self.server.listen()
        while True:
            self.conn, self.addr = self.server.accept()
            self.thread = threading.Thread(target=self.handle_client, args=(self.conn, self.addr))
            self.thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} ")

class client:
    def __init__(self):
        self.SERVER = '192.168.8.154'
        self.PORT = 1236
        self.ADDR = (self.SERVER, self.PORT)
        self.HEADER = 64
        self.FORMAT = 'utf-8'
        self.DISCONNECT = "diconnect"    

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, msg):
        self.message = msg.encode(self.FORMAT)
        self.msg_length = len(self.message)
        self.send_length = str(self.msg_length).encode(self.FORMAT)
        self.send_length += b' ' * (self.HEADER - len(self.send_length))
        self.client.send(self.send_length)
        self.client.send(self.message)

server_object = server()

thread_server = threading.Thread(target=server_object.start_server)
#thread_client = threading.Thread(target=client_object.send, args=(input("g")))
thread_server.start()
#thread_client.start()
while True:
    client_object = client()

    client_object.send(input("h:"))