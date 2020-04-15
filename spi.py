import spidev
from time import sleep
spi = spidev.spiDev(0,0)
def sendCommand(command: string):
	for char im command:
		spi.xfer(char, 1)


try:
	while(True):
		sendCommand("Left")
		sleep(2)

except KeyboardInterrupt:
	spi.close()
