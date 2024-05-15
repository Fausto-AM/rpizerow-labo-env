from gpiozero import PWMLED
import ADS1x15
import time
# Declara el pin de I2C y el registro
ads = ADS1x15.ADS1115(0,0x48)
# Declara el modo a utilizar.
ADS.setMode(ADS.MODE_SINGLE)
# Hace que la ganancia del ADC sea de +-6,144V.
ADS.setGain(ADS.PGA_4_096V)
# Convierte el valor obtenido por el ADC a un valor de voltaje.
factor = ADS.toVoltage()
# Pone la cantidad de muestras que va a recoger por segundo (7 = 860SPS)
setDataRate(7)

blue = PWMLED(26)
red = PWMLED(19)

while True :
	Pval = ADS.readADC(3)
	Tval = ADS.readADC(1)
	PvalV = Pval/factor
	TvalV = Tval/factor
	
	if (Pval > Tval) :
		red.value = value
	elif (Pval < Tval) :
		blue.value = value
	print("Temperatura del Termistor: {} " .format(Tval))
	print("Temperatura del Potenciómetro: {} ", .format(Pval))
	time.sleep(1)
