#!/usr/bin/env python3
import socket as S

def start_tcp_client():
    client_socket = S.socket(S.AF_INET6, S.SOCK_STREAM)

    # Automatically resolve the address and interface using getaddrinfo
    addr_info = S.getaddrinfo('fe80::9d6f:bd1a:a3f8:429b%wlan0', 8080, S.AF_INET6, S.SOCK_STREAM)
    
    # Connect using the address from getaddrinfo
    client_socket.connect(addr_info[0][4])  # addr_info[0][4] contains the address tuple
    message = client_socket.recv(1024)
    print(f"Received from server: {message.decode()}")
    client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
