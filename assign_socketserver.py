#!/usr/bin/env python3
import socket as S

def start_tcp_server():
        server_socket = S.socket(S.AF_INET, S.SOCK_STREAM)
        server_socket.bind(('192.168.43.200', 8080))
        server_socket.listen(5)
        print("TCP Server listening on port 8080")

        while True:
                client_socket, client_address = server_socket.accept()
                print(f"connection established with {client_address}")
                client_socket.send(b'Hello from TCP server! I am good')
                client_socket.close()

if __name__ == "__main__":
        start_tcp_server()
