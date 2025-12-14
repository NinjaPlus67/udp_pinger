from socket import *
import random

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", 12000))

print("UDP Pinger Server is running...")

while True:
    rand = random.randint(0, 10)
    message, clientAddress = serverSocket.recvfrom(1024)
    message = message.decode().upper()

    if rand < 2:
        continue

    serverSocket.sendto(message.encode(), clientAddress)
