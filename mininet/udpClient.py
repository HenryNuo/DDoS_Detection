import socket
import time


print('Please enter receiver ip address')
hostname = input()
print('Please enter repeat UDP pkt')
repeat = int(input())
serverAddressPort   = (hostname, 19999)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
# Send to server using created UDP socket
for i in range(repeat):
    msgFromClient       = 'Count' + str(i)
    time.sleep(0.01)
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
