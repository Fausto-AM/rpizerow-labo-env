#Importa el LED y el Boton para utilizarlos
from gpiozero import LED, Button
#Importa pause para que el código espere a la próxima instrucción
from signal import pause

#Declare que el LED a utilizar es el LED Rojo
led = LED(19)

#Utiliza el boton que está
button = Button(18)

#Cuando el boton esta presionado, prende el LED
button.when_pressed = led.on
#Cuando el boton no esta presionado, apaga el LED
button.when_released = led.off

#Pausa el programa
pause()
