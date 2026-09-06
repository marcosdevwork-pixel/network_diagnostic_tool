# imports
import socket
import time

# Socket creation
s = socket.socket()

 # define the port
port = 443

# user input 
host = input("Enter a hostname: ")

# tries the connection and shows its diagnosis
try:
    ip = socket.gethostbyname(host)

    start = time.perf_counter()

    s.connect((ip, port))

    end = time.perf_counter()

    connection_time = (end - start) * 1000
    print(f"Hostname: {host} \nIP:{ip} \nPort: {port}\n Connection time: {connection_time:.2f} ms")

except:
    print("Connection failed")
    




