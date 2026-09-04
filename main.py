# imports
import socket

# Socket creation
socket.socket()

# user input 
host = input("Enter a hostname: ")

# hostname ip search
ip = socket.gethostbyname(host)

# program output
print(f"Hostname: {host} | IP:{ip}")