import socket
import threading
# Function to simulate a server
def simulation_server () -> int :
    try :
        server_socket : tuple = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as msg:
        print("Socket creation failed")
        print(msg)

    server_socket.bind(('localhost', 0))
    server_socket.listen(1)  # Queue up to 1 requests
    port : tuple = server_socket.getsockname()[1] # Eg. ('127.0.0.1', 46617)
    print(f"Server listening on port {port}")

    # Accept a connection
    client_socket , addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    # Send a message
    client_socket.sendall(b"RMIT, This is the server!!!!!!")

    # Clean up
    client_socket.close()
    server_socket.close()

    return port

if __name__ == "__main__":
    # We'll run the server in a separate thread because accept() is blocking
    server_thread = threading.Thread(target=simulation_server )
    # Start the server
    server_thread.start()
