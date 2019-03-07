import socket, sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        host, port = sys.argv[1:3] # host = "www.google.com", port = 8080
        try:
            ip = socket.gethostbyname(host) # получение IP по доменному имени
        except socket.gaierror:
            print(f"Hostname {host} does not exist")
            sys.exit()
        print(f"IP address of {host}: {ip}")
        socket_desc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # настройка сокета
        try:
            socket_desc.connect((host, int(port))) # подключение с параметрами
        except KeyboardInterrupt:
            pass
        socket_desc.close()