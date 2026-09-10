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

dns_success = False
tcp_status = "Not tested"
tcp_error = ""
ip = "Not resolved"
connection_time = 0
ping_status = "Not tested"
packet_sent = 0
packets_received = 0
packet_lost = "N/A"
minimum = "N/A"
maximum = "N/A"
average = "N/A"
try:
    # DNS resolution
    ip = socket.gethostbyname(host)
    dns_success = True

except socket.gaierror as error:
    print(error)
    tcp_status = "not tested"
    tcp_error = "DNS resolution failed"

if dns_success == True:
    try:
        # TCP connection test
        start = time.perf_counter()

        s.connect((ip, port))

        end = time.perf_counter()

        connection_time = (end - start) * 1000
        tcp_status = "Successful"

    except ConnectionRefusedError as error:
        tcp_status = "Failed"
        tcp_error = "Connection refused"


try:
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

        if int(packets_received) > 0:
            ping_status = "Successful"
        else:
            ping_status = "Not tested"

           

except subprocess.SubprocessError as error:
    ping_error = str(error)



 # Diagnostic report
output = f"""
=======================================
        NETWORK DIAGNOSTIC
=======================================

TARGET:
    Hostname: {host}
    IP address: {ip}

TCP connection
    Status: {tcp_status}
    Port: {port}
    Connection time: {connection_time:.2f} ms

PING 
    Status: {ping_status}
    Packets sent: {packet_sent}
    Packets received: {packets_received}
    Packet loss: {packet_lost}
    Average latency: {average}
    Minimum latency: {minimum}
    Maximum latency: {maximum}

    """
print(output)




    




