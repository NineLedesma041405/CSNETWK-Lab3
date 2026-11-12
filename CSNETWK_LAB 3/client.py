import socket


CLIENT_NAME = "Client of John Doe"
HOST = '192.168.1.17'
# host = socket.gethostbyname(socket.gethostname()
PORT = 6523

def start_client():
    client_socket = None
    try:
        user_input = int(input("Enter int (1 - 100): "))

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        client_socket.connect((HOST, PORT))

        message = f"{CLIENT_NAME},{user_input}"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent message '{message}'")

        reply = client_socket.recv(1024).decode('utf-8')
        
        if not reply:
            print("Server terminated the connection.")
            return
        
        print(f"Received server response: '{reply}'.")

        server_name, server_int_str = reply.rsplit(',',1)
        server_int = int(server_int_str)

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

    except ValueError:
        print("Enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occured: {e}.")

    finally:
        if client_socket:
            client_socket.close()
            print("Client socket closed successfully.")  



if __name__ == "__main__":
    start_client()