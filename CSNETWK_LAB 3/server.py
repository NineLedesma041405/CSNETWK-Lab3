import socket
import random
import threading

SERVER_NAME = "Server of John Doe"
HOST = '192.168.1.17'
# host = socket.gethostbyname(socket.gethostname())
PORT = 6523

def handle_client(communication_socket, address, server):

    try:
        message = communication_socket.recv(1024).decode('utf-8')
        if not message:
            communication_socket.close()
            return

        client_name, client_int_str = message.rsplit(',',1)
        client_int = int(client_int_str)
        print(f"Received connection from {client_name}")
        print(f"Server Name: {SERVER_NAME}")

        if (client_int < 1 or client_int > 100):
            print(f"{client_int} is out of range.")
            communication_socket.close() 
            server.close()
            return

        server_int = random.randint(1,100)
        total_sum = client_int + server_int

        print(f"Client Number: {client_int} | Server Number: {server_int} | Total Sum: {total_sum}")

        communication_socket.send(f"{SERVER_NAME},{server_int}".encode('utf-8'))
        communication_socket.close()
        print(f"Connection with {address} ended!")

    except Exception as e:
        print(f"An unexpected error occured: {e}.") 


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        try: 
            communication_socket, address = server.accept()
            print(f"Connected to: {address}")
            threading.Thread(target=handle_client, args=(communication_socket, address, server)).start()

        except:
            break

if __name__ == "__main__":
    start_server()