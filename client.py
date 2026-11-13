import socket

# Initializing details
CLIENT_NAME = "Client of Kirsten Ledesma & Mikaella Martinez"
HOST = '127.0.0.1'
# host = socket.gethostbyname(socket.gethostname()
PORT = 6523

def start_client():
    client_socket = None # placeholder variable
    try:
        # program asks user for integer input
        user_input = int(input("Enter int (1 - 100): "))

        # creating a client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect client to server 
        client_socket.connect((HOST, PORT))

        # sends client data to server
        message = f"{CLIENT_NAME},{user_input}"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent message '{message}'")

        # it receives and decodes the server reply
        reply = client_socket.recv(1024).decode('utf-8')
        
        if not reply:
            print("Server terminated the connection.")
            return
        
        print(f"Received server response: '{reply}'.")

        # initialize and split the data from server reply
        server_name, server_int_str = reply.rsplit(',',1)
        server_int = int(server_int_str)

        # to deal with Out-Of-Bounds errors and print results
        if server_int < 1 or server_int > 100:
            print(f"{server_int_str} is out of range.")
        else:
            total_sum = user_input + server_int
            print("RESULTS")
            print(f"Client Name: {CLIENT_NAME}")
            print(f"Server Name: {server_name}")
            print(f"Client Value: {user_input}")
            print(f"Server Value: {server_int}")
            print(f"Sum: {total_sum}")

    # occurs if user inputs invalid integer
    except ValueError:
        print("Enter a valid integer.")
    # catches specific exceptions 
    except Exception as e:
        print(f"An unexpected error occured: {e}.")

    # closes client socket
    finally:
        if client_socket:
            client_socket.close()
            print("Client socket closed successfully.")  



if __name__ == "__main__":
    start_client()