import socket


HOST = '94.140.232.97'
PORT = 25565

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))


while True:
    sock.send('[~] Connected client'.encode("utf-8"))

    data = sock.recv(1024).decode("utf-8")
    print(data)