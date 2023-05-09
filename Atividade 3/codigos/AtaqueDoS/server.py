import socket
import threading

# Cria um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Endereço e porta do servidor
server_address = ('localhost', 5555)

# Liga o socket à porta
server_socket.bind(server_address)

# Coloca o socket em modo de escuta
server_socket.listen(5)

# Lista para armazenar as conexões dos clientes
client_connections = []

# Função que lida com as conexões dos clientes
def handle_client(client_socket, client_address):
    print(f"Nova conexão de {client_address}")

    # Adiciona a conexão do cliente à lista
    client_connections.append(client_socket)

    while True:
        # Recebe a mensagem do cliente
        message = client_socket.recv(1024).decode()

        if not message:
            # Se a mensagem estiver vazia, desconecta o cliente e remove a conexão da lista
            print(f"{client_address} desconectado")
            client_socket.close()
            client_connections.remove(client_socket)
            break

        # Exibe a mensagem no console
        print(f"Mensagem de {client_address}: {message}")

# Loop principal do servidor
while True:
    # Espera por uma nova conexão
    client_socket, client_address = server_socket.accept()

    # Inicia uma nova thread para lidar com a conexão do cliente
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()