import socket

# Criação do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8888))

servidor.listen()
cliente, endereco = servidor.accept()

# Declaração de variávies
terminado = False

# Main

while not(terminado):
    msg = cliente.recv(1024).decode('utf-8')
    
    if (msg == 'finalizar chat'):
        terminado = True
    else:
        print(f"Cliente: {msg}")
    
    cliente.send(input('Mensagem: ').encode('utf-8'))

servidor.close()
cliente.close()
