import socket

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 65432      # Port to listen on

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Server listening...')
        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    data = conn.recv(1024)
                    if data:
                        print("Received clipboard data:", data.decode('utf-8'))
                        uppercase_data = data.decode('utf-8').upper()
                        conn.sendall(uppercase_data.encode('utf-8'))
        except KeyboardInterrupt:
            print("\nServer is shutting down...")

if __name__ == '__main__':
    main()
