#Importa lo necesario para utilizar los LEDs
from gpiozero import LED
#Importa lo necesario para permitir que haya un tiempo de espera
from time import sleep

#Nombres de las variables de los LEDs
ledr = LED(19)
leda = LED(26)
ledv = LED(13)

#Bucle para que el programa no pare de funcionar
while True:
	#Prende el LED Rojo
	ledr.on()
	#Espera 1 segundo
	sleep(1)
	#Apaga el LED Rojo
	ledr.off()
	#Prende el LED Azul
	leda.on()
	#Espera 0.5 segundos
	sleep(0.5)
	#Apaga el LED Azul
	leda.off()
	#Prende el LED Verde
	ledv.on()
	#Espera 0.25 segundos
	sleep(0.25)
	#Apaga el LED Vered
	ledv.off()
	#Espera 1 segundo para volver a empezar el bucle
	sleep(1)
