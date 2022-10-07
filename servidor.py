from concurrent.futures import thread
import socket
import threading

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 8888))
servidor.listen()

clientes = []
usernames = []

def transmitir(mensagem):
    for cliente in clientes:
        cliente.send(mensagem)

def gerencia(cliente):
    while (True):
        try:
            mensagem = cliente.recv(1024)
            transmitir(mensagem)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            username = usernames[index]
            transmitir(f"{username} saiu do chat.".encode('utf-8'))
            usernames.remove(username)
            break

def recebe():
    while (True):
        cliente, endereco = servidor.accept()
        print(f"Conectado com {endereco}")

        cliente.send("UN".encode('utf-8'))
        username = cliente.recv(1024).decode('utf-8')
        usernames.append(username)
        clientes.append(cliente)

        print(f"Nome de usuário do cliente é {username}")

        transmitir(f"{username} se conectou ao servidor".encode('utf-8'))
        cliente.send("Conectado ao servidor.".encode('utf-8'))

        thread = threading.Thread(target=gerencia, args=(cliente,))
        thread.start()
        
print("O servidor está escutando...")
recebe()