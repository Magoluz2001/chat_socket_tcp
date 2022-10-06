import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 8888))

terminado = False

print("Digite 'finalizar chat' para encerrar a conexão.")
while not(terminado):
    cliente.send(input('Mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')

    if (msg == 'finalizar chat'):
        terminado = True
    else:
        print(f"Servidor: {msg}")

cliente.close()