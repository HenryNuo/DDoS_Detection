import socket
import time

print("input receiver address")
HOST = input()
print("input count to send")
COUNT = int(input())
PORT = 12345
BUFSIZE = 4096

def send_bytes(count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print((HOST, PORT))
        sock.settimeout(100)
        sock.connect((HOST, PORT))
    except socket.error as err:
        print(err, HOST, PORT)
        sock.close()
        return
    for i in range(count * 2):
        sent = sock.send(bytes(('Count '+ str(i)), 'utf-8'))
        time.sleep(0.5)

def send_file(fname):
    with open(fname, 'rb') as f:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print((HOST, PORT))
            sock.settimeout(100)
            sock.connect((HOST, PORT))
        except socket.error as err:
            print(err, HOST, PORT)
            sock.close()
            return

        while True:
            data = f.read(BUFSIZE)
            if not data:
                break
            while data:
                sent = sock.send(data)
                data = data[sent:]

    sock.close()

def main():
    # send_file('send.txt')
    send_bytes(COUNT)

if __name__ == '__main__':
    main()