import socket
import threading


HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Whatever IP address you found from running ifconfig in terminal.
#SERVER = "10.1.13.181" #IP para conectar com o servidor
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Officially connecting to the server.
client.connect(ADDR)

def handle_client():
    print(client.recv(2048).decode(FORMAT))


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


while True:
    mensagem = input()
    send(mensagem)
    thread = threading.Thread(target=handle_client)
    thread.start()
    if mensagem == '0': break

send(DISCONNECT_MESSAGE)
