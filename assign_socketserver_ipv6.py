#!/usr/bin/env python3
import socket as S

def start_tcp_server():
    server_socket = S.socket(S.AF_INET6, S.SOCK_STREAM)
    
    # Automatically resolve address and interface using getaddrinfo
    addr_info = S.getaddrinfo('fe80::9d6f:bd1a:a3f8:429b%wlan0', 8080, S.AF_INET6, S.SOCK_STREAM)
    
    # Bind using the address from getaddrinfo
    server_socket.bind(addr_info[0][4])  # addr_info[0][4] contains the bind address
    server_socket.listen(5)
    print("TCP Server listening on port 8080")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        client_socket.send(b'Hello from TCP server! I am good')
        client_socket.close()

if __name__ == "__main__":
    start_tcp_server()
