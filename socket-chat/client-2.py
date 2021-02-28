import socket, threading

def handle_messages(connection: socket.socket):
    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break

def client(username) -> None:
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 25213 # ID: 6130521321

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        threading.Thread(target=handle_messages, args=[socket_instance]).start()

        print('Connected to chat!')

        while True:
            msg_input = input()
            msg_send = f"{username} : {msg_input}"
            print(msg)

            if msg_input == 'quit':
                break

            socket_instance.send(msg_send.encode())

        socket_instance.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


if __name__ == "__main__":
    username = input("Set your username: ")
    client(username)
