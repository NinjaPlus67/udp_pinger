from socket import *
import time

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

TOTAL_PINGS = 4

sent = 0
received = 0
rtts = []

for i in range(1, TOTAL_PINGS + 1):
    sent += 1
    sendTime = time.time()
    message = f"Ping {i} {sendTime}"
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        response, address = clientSocket.recvfrom(1024)
        recvTime = time.time()

        rtt = recvTime - sendTime
        rtts.append(rtt)
        received += 1

        print(f"Reply: {response.decode()} | RTT = {rtt*1000:.2f} ms")

    except timeout:
        print(f"Ping {i}: Request timed out.")

clientSocket.close()


lost = sent - received
loss_percent = (lost / sent) * 100
delivery_percent = (received / sent) * 100

print("\n--- UDP Pinger Statistics ---")
print(f"Packets sent:     {sent}")
print(f"Packets received: {received}")
print(f"Packets lost:     {lost}")
print(f"Packet loss:      {loss_percent:.1f}%")
print(f"Delivery rate:    {delivery_percent:.1f}%")

if rtts:
    min_rtt = min(rtts) * 1000
    max_rtt = max(rtts) * 1000
    avg_rtt = (sum(rtts) / len(rtts)) * 1000
    print("\n--- RTT (ms) ---")
    print(f"Min RTT: {min_rtt:.2f} ms")
    print(f"Max RTT: {max_rtt:.2f} ms")
    print(f"Avg RTT: {avg_rtt:.2f} ms")
else:
    print("\nNo replies received, so RTT stats are unavailable.")

    sendTime = time.time()
    message = f"Ping {i} {sendTime}"
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        response, address = clientSocket.recvfrom(1024)
        recvTime = time.time()
        rtt = recvTime - sendTime

        print(f"Reply from server: {response.decode()}  RTT = {rtt:.4f} sec")

    except timeout:
        print("Request timed out.")
print ()
clientSocket.close()
