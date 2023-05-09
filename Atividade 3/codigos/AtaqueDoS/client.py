import socket
import threading
import time
import random
import string

# Cria um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Endereço e porta do servidor
server_address = ('localhost', 5555)

# Conecta-se ao servidor
client_socket.connect(server_address)

# o K recebe o tamanho da string que pode ser alterado
messages = [''.join(random.choices(string.ascii_letters, k=1))]

# Função que envia as mensagens para o servidor
def send_messages():
    while True:
        # Espera por um período de tempo aleatório entre 1 e 5 segundos
        time.sleep(0.00002)

        # Seleciona uma mensagem aleatória da lista
        message = random.choice(messages)

        # Envia a mensagem para o servidor
        client_socket.sendall(message.encode())

# Inicia a thread que envia as mensagens
threading.Thread(target=send_messages).start()
