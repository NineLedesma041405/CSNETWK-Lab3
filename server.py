import socket
import random
import threading

# Initialize server details like server name, host address, port address
SERVER_NAME = "Server of Kirsten Ledesma & Mikaella Martinez"
HOST = '127.0.0.1'
# host = socket.gethostbyname(socket.gethostname()) -> when opened by different computers
PORT = 6523

def handle_client(communication_socket, address, server):

    # for exception handling
    try:

        # receive data from the socket
        message = communication_socket.recv(1024).decode('utf-8')
        # closes the connection if not message not found or no data received
        if not message:
            communication_socket.close()
            return

        # initialize and split the data 
        client_name, client_int_str = message.rsplit(',',1)
        client_int = int(client_int_str)
        print(f"Received connection from {client_name}")
        print(f"Server Name: {SERVER_NAME}")

        # to deal with Out-Of-Bounds errors
        if (client_int < 1 or client_int > 100):
            print(f"{client_int} is out of range.")
            communication_socket.close() 
            server.close()
            return

        # to make the server pick a random integer from 1-100
        # and calculate total sum from integers selected by client and server
        server_int = random.randint(1,100)
        total_sum = client_int + server_int

        # prints the results
        print(f"Client Number: {client_int} | Server Number: {server_int} | Total Sum: {total_sum}")

        # send data to client
        communication_socket.send(f"{SERVER_NAME},{server_int}".encode('utf-8'))
        # close the connection
        communication_socket.close()
        print(f"Connection with {address} ended!")

    # catches specific exceptions 
    except Exception as e:
        print(f"An unexpected error occured: {e}.") 


def start_server():

    # creating a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binding and listening
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        try: 
            # establishing a connection with client
            communication_socket, address = server.accept()
            print(f"Connected to: {address}")
            # constructing thread for multi-threading 
            threading.Thread(target=handle_client, args=(communication_socket, address, server)).start()
        except:
            break

if __name__ == "__main__":
    start_server()