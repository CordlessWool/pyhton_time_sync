import pdb
import socket
import time
import os
UDP_IP_IN = "192.168.188.24"
UDP_IP_MASTER = "192.168.188.20"
UDP_PORT = 5005
#MESSAGE = time.time()

os.nice(0)
print("My process id %d" % os.getpid())
os.system("chrt -f -p 98 %d" % os.getpid())

print ("UDP target IP: %s" %UDP_IP_IN)
print ("UDP master IP: %s" %UDP_IP_MASTER)
print ("UDP target port:%d" %UDP_PORT)
#print("message:", MESSAGE)

data = ""
timeToWait = 3 #time in seconds

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_IN, UDP_PORT))
sock.settimeout(3)

#class MissingMessage(Exception): pass
while True:
	
	print("Start requesting for new Time")	
	sock.sendto('get_time', (UDP_IP_MASTER, UDP_PORT))
	
	try:	
		data = ""
	
		data, addr = sock.recvfrom(50)
		sock.sendto(data, addr)
		
		data = ""
		data, addr = sock.recvfrom(50)
		
		print("%.20f " % time.time())
		print(data)
		os.system("date -s @%s" % data)
		print("new Time: %.20f " % time.time())
	
	except:
		print("missed message")
	
	time.sleep(10)
	
