import socket
import threading
from sys import argv
import time

PORT = 20000

def recieve_the_file():
    global PORT
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", PORT))
    file_name = str(time.time())
    while True:
        data, addr = sock.recvfrom(1024)
        if data:
            print("data recieved from %s" % addr)
            with open(file_name, 'a') as fw:
                fw.write(data)
        else:
            file_name = str(time.time())

if __name__ == "__main__":
    print(len(argv))
    if len(argv) > 3:
        command = argv[1]
        file_path = argv[2]
        TO_IP = argv[3]

        if command == 'recv':
            thread = threading.Thread(target=recieve_the_file)
            thread.start()
        elif command == 'send':
            sock_to = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock_to.bind((TO_IP, PORT))
            try:
                with open(file_path, 'rb') as fr:
                    for line in fr:
                        sock_to.sendto(line, (TO_IP, PORT))

            except Exception as e:
                print(str(e))
        else:
            print("Enter a valid command from <send/recv>")

    else:
        print("[./main.py <command> <file_path> <to_ip>]") 
