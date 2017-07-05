#this is time master

import socket
import time
import os

os.nice(0)
print("My process id %d" % os.getpid())
os.system("chrt -f -p 99 %d" % os.getpid())

UDP_IP_OWN = "192.168.188.20"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("I am the master of all Raspberry timestamps")
print("I am listening on %s:%d" %(UDP_IP_OWN, UDP_PORT))

### bind socket to listen on port and 
sock.bind((UDP_IP_OWN, UDP_PORT))

data = ""
addr = []

while True:
	
	data, addr = sock.recvfrom(50)
	
	print("requested for " + str(data))	
	
	if data == "get_time":
		#send timestamp string with 20 number behind .
		sock.sendto(str("%.20f" % time.time()), addr)
	else:
		delay = time.time() - float(data)
		newTime = time.time()+(delay/2)
		sock.sendto(str("%.20f" % newTime), addr)
		print("\nDelay and new time")
		print(delay)
		print(str("%.20f" % newTime))		
		print(str("%.20f" % time.time()))		
