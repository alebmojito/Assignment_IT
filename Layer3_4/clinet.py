import socket
def simulate_client(port) -> str :
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', port))

    # Receive a message from the server
    msg = client_socket.recv(1024) # Receive no more than 1024 bytes
    print(f"Client received {msg.decode()}")

    # Clean up
    client_socket.close()
    return msg.decode("utf-8")



if __name__ == '__main__':
    try:
        server_port = 64975
        # Run the client simulation to connect to the server
        simulate_client(server_port)
    except ConnectionRefusedError as e:
        print(e)
