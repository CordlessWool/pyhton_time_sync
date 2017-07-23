import time
import pygame
import os

CORE_ID = 2
FIFO_LEVEL = 90


os.nice(0)
print("My process id %d" % os.getpid())

print("Set scheduling fifo level to %d" % FIFO_LEVEL)
os.system("chrt -f -p %d %d" % (FIFO_LEVEL, os.getpid()))

#print("Set affinity to core %d" % CORE_ID)
#os.system("taskset -cp %d %d" % (CORE_ID, os.getpid()))

pygame.mixer.init()
pygame.mixer.music.load("sweap1.wav")
#pygame.mixer.music.load("zusammensweap.wav")
stopIt = False
while True:
	if (time.time()%5) < 0.00001:
		#print "%.20f" % time.time()
		pygame.mixer.music.play()
		time.sleep(1)
		stopIt = True
	elif stopIt:
		pygame.mixer.music.stop()
		stopIt = False
		time.sleep(2)

#	while pygame.mixer.music.get_busy() == True:
#		continue    	
#	time.sleep(2.5)
#	pygame.mixer.music.stop()
#	time.sleep(5)

