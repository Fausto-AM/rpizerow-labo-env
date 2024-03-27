from gpiozero import LED
from time import sleep

ledr = LED(19)
leda = LED(26)
ledv = LED(13)

while True:
	ledr.on()
	sleep(1)
	ledr.off()
	leda.on()
	sleep(0.5)
	leda.off()
	ledv.on()
	sleep(0.25)
	ledv.off()
	sleep(1)
