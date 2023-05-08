import socket
import ifcfg

for name, interface in ifcfg.interfaces().items():
    if 'eth0' in name:
        hostname    = interface['inet']
        break
print(hostname)
PORT = 12345
BUFSIZE = 4096
        
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind((hostname, PORT))
    except socket.error as err:
        print('Bind failed', err)
        return

    sock.listen(1)
    print('Socket now listening at', hostname, PORT)
    # receive_file(sock)
    receive_bytes(sock)
    
def receive_file(sock):
    file_number = 0
    try:
        while True:
            conn, addr = sock.accept()
            print('Connected with', addr)

            fname = 'received%d.txt' % file_number
            with open(fname, 'wb') as f:
                while True:
                    data = conn.recv(BUFSIZE)
                    if not data:
                        break
                    f.write(data)
            conn.close()
            print(fname, 'saved\n')
            file_number += 1

    # Hit Break / Ctrl-C to exit
    except KeyboardInterrupt:
        print('\nClosing')

    sock.close()

def receive_bytes(sock):
    try:
        while True:
            conn, addr = sock.accept()
            print('Connected with', addr)
            while True:
                data = conn.recv(BUFSIZE)
                print(data)
                if not data:
                    break
            conn.close()

    # Hit Break / Ctrl-C to exit
    except KeyboardInterrupt:
        print('\nClosing')

    sock.close()

if __name__ == '__main__':
    main()