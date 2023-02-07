import socket

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to a specific IP address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

# Accept incoming connections
client_socket, client_address = server_socket.accept()

# Create a socket for communication with the main computer
main_computer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the main computer socket to the main computer's IP address and port
main_computer_address = ('localhost', 56789)
main_computer_socket.connect(main_computer_address)

# Receive data from the client
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    data = data.decode()
    # Split the received data into command type and value
    command_type, value = data.split(":")
    # Process the command based on the type
    if command_type == "mouse":
        # Split the value into x and y coordinates
        x, y = map(int, value.split(","))
        # Construct a dictionary with the decoded mouse coordinates and type
        mouse_data = {"type": "mouse", "x": x, "y": y}
        # Send the mouse data to the main computer
        main_computer_socket.send(str(mouse_data).encode())
    elif command_type == "keyboard":
        # Split the value into key and duration
        key, duration = value.split(",")
        duration = float(duration)
        # Construct a dictionary with the decoded keyboard command and type
        keyboard_data = {"type": "keyboard", "key": key, "duration": duration}
        # Send the keyboard data to the main computer
        main_computer_socket.send(str(keyboard_data).encode())

# Close the client and main computer sockets
client_socket.close()
main_computer_socket.close()
