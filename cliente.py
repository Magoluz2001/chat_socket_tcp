from asyncore import write
from http import client
import socket
import threading

username = input('Escolha um nome de usuário: ')

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8888))

def recebe():
    while (True):
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            if (mensagem == 'UN'):
                cliente.send(username.encode('utf-8'))
            else:
                print(mensagem)
        except:
            print('Ocorreu um erro.')
            cliente.close()
            break

def escreve():
    while (True):
        mensagem = f"{username}: {input('')}"
        cliente.send(mensagem.encode('utf-8'))

recebe_thread = threading.Thread(target=recebe)
recebe_thread.start()

escreve_thread = threading.Thread(target=escreve)
escreve_thread.start()