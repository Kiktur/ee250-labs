"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

HOST = "10.203.172.246"
PORT = 10000

def main():

    # Creates socket using IPv4 with TCP connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connects at IP address "HOST" using port number "PORT"
        s.connect((HOST, PORT))

        # Prompts user for a message to send
        message = input("Write your message to the server: ")

        # Encodes message as bytes
        message_bytes = message.encode("utf-8")

        # Sends full message and waits for a response
        s.sendall(message_bytes)
        data = s.recv(1024)

    print(f"Received {data!r}")


    # TODO: Get user input and send it to the server using your TCP socket
    # TODO: Receive a response from the server and close the TCP connection
    pass


if __name__ == '__main__':
    main()