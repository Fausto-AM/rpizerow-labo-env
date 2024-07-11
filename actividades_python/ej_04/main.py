from gpiozero import PWMLED
import ADS1x15
import time
import math

# Declara el pin de I2C y el registro
ADS = ADS1x15.ADS1115(1,0x48)
# Declara el modo a utilizar.
ADS.setMode(ADS.MODE_SINGLE)
# Hace que la ganancia del ADC sea de +-6,144V.
ADS.setGain(ADS.PGA_4_096V)
# Convierte el valor obtenido por el ADC a un valor de voltaje.
factor = ADS.toVoltage()

# Declara que los pines 26 y 19 corresponden al LED rojo y azul y permite variar su brillo usando PWM.
blue = PWMLED(26)
red = PWMLED(19)

# Variables a usar para el cálculo de Temperatura.
## vcc  = Fuente
vcc = 3.3
## vrt = Voltaje sobre el Termistor
vrt = 0
## rt = Resistencia del Termistor
rt = 0
## t = Temperatura base
t = 0
## r = Resistencia R1 del divisor de tensión con el Termistor.
r = 10000
## Factor de aumento del Termistor.
beta = 3977

while True :

	# Hace que el ADC lea en el pin 3 (Potenciómetro) y en el pin 1 (Termistor)
	Pval = ADS.readADC(3)
	Tval = ADS.readADC(1)
	# Multiplica el valor obtenido del Potenciómetro y del Termistor por el factor de incremento del ADC.
	PvalV = Pval * factor
	TvalV = Tval * factor

	# Cálculo de Temperatura.
	vrt = (3.3*TvalV)/4095
	rt = r/((vcc/vrt)-1)
	t = beta/(math.log10(rt/r)+(beta/298.0))
	t = t - 273.15

	# El brillo del LED rojo aumenta y disminuye dependiendo de si la diferencia de la temperatura del
	# Potenciómetro es mayor de la del Termistor hasta un máximo de 5 grados, en la que será el máximo posible.
	if (PvalV>TvalV):
		red.value = (PvalV-TvalV)*0.2

		if (red.value>1):
			red.value = 1
		time.sleep(1)
	# El brillo del LED azul aumenta y disminuye dependiendo de si la diferencia de la temperatura del
	# Termistor es mayor de la del Potenciómetro hasta un máximo de 5 grados, en la que será el máximo posible.
	elif (PvalV<TvalV):
		blue.value = (TvalV-PvalV)*0.2

		if (blue.value>1):
			blue.value = 1
		time.sleep(1)
	# En caso de que la temperatura configurada sea igual a la que sea medida, el valor del brillo los LEDs
	# será 0.
	else:
		blue.value = 0
		red.value = 0
		time.sleep(1)
		
	# Muestra los valores que el usuario desea conocer.
	print("Valor del Termistor {0:.3f} V".format(TvalV))
	print("Valor del Potenciómetro {0:.3f} V".format(PvalV))
	print("Valor  del Termistor {0:.3f} T".format(t))

	time.sleep(1)
