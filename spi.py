import spidev
from random import randint
from time import sleep
commands = ["Left", "Right", "Stop"]
spi = spidev.spiDev(0,0)
def sendCommand(command: string):
	for char in command:
		spi.xfer(char, 1)


try:
	while(True):
		sendCommand(commands[randint(1, 3)])
		sleep(3)

except KeyboardInterrupt:
	spi.close()
