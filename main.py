# imports
import socket

# Socket creation
s = socket.socket()

 # define the port
port = 443

# user input 
host = input("Enter a hostname: ")

# tries the connection and shows its diagnosis
try:
    ip = socket.gethostbyname(host)

    s.connect((ip, port))
    print(f"Hostname: {host} \nIP:{ip} \nPort: {port}")

except:
    print("Connection failed")
    




