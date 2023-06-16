import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

ip_address = str(sys.argv[1])
port = int(sys.argv[2])

server.connect((ip_address, port))


while True:

    message = input("Type your message: ")
    server.send(bytes(message, "utf-8"))

    


server.close()