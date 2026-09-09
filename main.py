# Imports
import socket
import time
import subprocess

# Socket creation
s = socket.socket()

# Port to test
port = 443

# User input 
host = input("Enter a hostname: ")

# Network diagnosis
try:
    # DNS resolution
    ip = socket.gethostbyname(host)

    # TCP connection test
    start = time.perf_counter()

    s.connect((ip, port))

    end = time.perf_counter()

    connection_time = (end - start) * 1000

    # Ping test
    ping_results = subprocess.run(
            ["ping", host],
            capture_output=True,
            text=True
        )

    lines = ping_results.stdout.splitlines()

    # Extract packet statistics and latency
    for line in lines:
        if "Packets" in line:
            parts = line.split()

            packet_sent = parts[3].replace(",", "")
            packets_received = parts[6].replace(",", "")
            packet_lost = parts[10].replace("(", "")

        if "Minimum" in line:
            parts = line.split()

            minimum = parts[2].replace(",", "")
            maximum = parts[5].replace(",", "")
            average  = parts[8]
     
# Diagnostic report
    output = f"""
=======================================
          NETWORK DIAGNOSTIC
=======================================

TARGET:
    Hostname: {host}
    IP address: {ip}

TCP connection
    Status: Successful
    Port: {port}
    Connection time: {connection_time:.2f} ms

PING 
    Status: Successful
    Packets sent: {packet_sent}
    Packets received: {packets_received}
    Packet loss: {packet_lost}
    Average latency: {average}
    Minimum latency: {minimum}
    Maximum latency: {maximum}

    """
    print(output)

except:
    print("Connection failed")
    




