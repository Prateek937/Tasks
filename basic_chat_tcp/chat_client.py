import socket
import threading

class client:
    def __init__(self):
        self.SERVER = "192.168.163.126"
        self.PORT = 1234
        self.ADDR = (self.SERVER, self.PORT)
        self.HEADER = 64
        self.FORMAT = 'utf-8'
        self.DISCONNECT = "diconnect"

        #self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = socket.socket()
        self.client.connect(self.ADDR)

    def send_msg(self):
        # sending messages to the server
        while True:
            self.msg = input()
            self.message = self.msg.encode(self.FORMAT)
            self.msg_length = len(self.message)
            self.send_length = str(self.msg_length).encode(self.FORMAT)
            self.send_length += b' ' * (self.HEADER - len(self.send_length))
            self.client.send(self.send_length)
            self.client.send(self.message)

    def recv_msg(self):
        # receiving the message length first for the header of the message
        # in case the message is too long or too short.
        self.connected = True
        while self.connected:
            self.msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
            if self.msg_length:
                self.msg_length = int(self.msg_length)

                # receiving message of the full length  
                self.msg = self.client.recv(self.msg_length).decode(self.FORMAT)
                if self.msg == self.DISCONNECT:
                    self.connection = False
                if self.msg != "":
                    print(f"[{self.SERVER}] {self.msg}")
        self.client.close()

    # for starting the chat
    def start_chat(self):
        thread_send = threading.Thread(target=self.send_msg)
        thread_recv = threading.Thread(target=self.recv_msg)
        thread_send.start()
        thread_recv.start()

client_obj = client()
client_obj.start_chat()
#more
