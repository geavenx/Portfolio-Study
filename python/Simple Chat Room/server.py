import socket
import select
import sys
from _thread import *

# O primeiro argumento do socket (AF_INET) é o endereço de domínio do socket. 
# O segundo argumento é o tipo de socket, nesse caso SOCK_STREAM, que significa que os dados são lidos em um fluxo contínuo.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# Checa se o número de argumentos fornecidos está correto
if len(sys.argv) != 3:


    print("Correct usage: script, IP address, port number")
    exit()


# Atribui os argumentos às suas respectivas variáveis
ip_address = str(sys.argv[1])
port = int(sys.argv[2])


# Associa o socket a porta local do servidor
server.bind((ip_address, port))


# Espera por 100 conexões ativas (número que pode variar pela conveniência)
server.listen(100)


list_of_clients = []


def client_thread(conn, addr):
    

    # Envia uma conexão ao cliente
    conn.send("Bem-vindo ao bate-papo!")

    
    while True:
        try:
            
            # .recv(Buffer)
            message = conn.recv(2048)
            
            
            if message:
                
                message_to_send = f"<{addr[0]}> {message}"

                # Printa a mensagem, e o endereço do usuário que enviou a mensagem
                print(f"<{addr[0]}> {message}")

                # Usa a função broadcast para enviar a mensagem a todos
                broadcast(message_to_send, conn)

            else:
                # Se a conexão estiver quebrada, removemos a conexão
                remove(conn)
        except:
            continue

# Usando a função abaixo, conseguimos fazer um broadcast da mensagem para todos os clientes, menos o que enviou-a
def broadcast(message, connection):
    for client in list_of_clients:
        if client != connection:
            try:
                client.send(message)
            except:
                client.close()

                # se o link estiver quebrado, removemos o cliente
                remove(client)

# A função abaixo simplesmente remove o cliente da lista de clientes que criamos no começo do programa
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    
    # Aceita o "request" de conexão e armazena dois parâmetros, conn (o socket de quem fez o request), e addr (endereço IP do cliente que conectou)
    conn, addr = server.accept()


    # Mantém a lista de clientes para fazer o broadcast
    list_of_clients.append(conn)


    # Printa o endereço do usuário que se conectou
    print(f"{addr[0]} connected")


    # Cria uma thread para cada usuário que conectar
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()