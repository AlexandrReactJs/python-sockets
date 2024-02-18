import socket


HOST = '0.0.0.0'
PORT = 25565


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)


while True: 
    conn, addr = sock.accept()
    
    conn.send('[~] Connected server'.encode("utf-8"))

    data = conn.recv(1024).decode("utf-8")
    print(data)


 