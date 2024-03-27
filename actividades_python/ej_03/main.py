#Importa lo necesario para utilizar el LED y el Buzzer
from gpiozero import LED, Buzzer

#Declara los puertos a usar para cada uno de los LEDs y el Buzzer
red = LED(19)
green = LED(13)
blue = LED(26)
buzzer = Buzzer(22)

#Crea un bucle para que el programa corra continuamente
while True:
	#Pide al usuario un prompt para utilizar
	inst  = input("Ingrese comando y opción: ")
	#Prende el buzzer
	if inst == "buzz on":
		buzzer.on()
	#Apaga el buzzer
	elif inst == "buzz off":
		buzzer.off()
	#Prende el LED Rojo
	elif inst == "rgb red":
		red.on()
	#Prende el LED Azul
	elif inst == "rgb blue":
		blue.on()
	#Prende el LED Verde
	elif inst == "rgb green":
		green.on()
	#En caso de que no se ponga alguno de los inputs, muestra un error.
	else:
		 print("error")
