import socket
import ifcfg

for name, interface in ifcfg.interfaces().items():
    if 'eth0' in name:
        hostname    = interface['inet']
        break
print(hostname)
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 

# Bind to address and ip
UDPServerSocket.bind((hostname, localPort))
print("UDP back ground server up and listening")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    # print(clientMsg)
    # print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)