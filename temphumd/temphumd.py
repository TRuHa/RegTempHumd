#!/usr/bin/env python3

from time import sleep, strftime

import RPi.GPIO as GPIO
import configparser
import dht11

config = configparser.ConfigParser()
seccion   = config.sections()

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

try:
	while True:
		#Establece fecha
		config.read('/home/pi/Python/TempHumd/medicion.cfg')

		datenow = strftime('%d_%m_%y')
		dato1   = config.items('DATO_1')
		lista   = ['fecha', 'hora', 'tempnow', 'humdnow', 'tempmax', 'tempmin', 'humdmax', 'humdmin']
		
		if not datenow in dato1[0]:
			i = 19
			while i != 0:
				dato = "DATO_" + str(i)
				print(dato)

				fecha = config.get(dato, lista[0])
				hora = config.get(dato, lista[1])
				tempnow = config.get(dato, lista[2])
				humdnow = config.get(dato, lista[3])
				tempmax = config.get(dato, lista[4])
				tempmin = config.get(dato, lista[5])
				humdmax = config.get(dato, lista[6])
				humdmin = config.get(dato, lista[7])

				i += 1
				dato = "DATO_" + str(i)
				print(dato)

				config.set(dato, lista[0], fecha)
				config.set(dato, lista[1], hora)
				config.set(dato, lista[2], tempnow)
				config.set(dato, lista[3], humdnow)
				config.set(dato, lista[4], tempmax)
				config.set(dato, lista[5], tempmin)
				config.set(dato, lista[6], humdmax)
				config.set(dato, lista[7], humdmin)

				i -= 2

			config.set("DATO_1", lista[4], '0')
			config.set("DATO_1", lista[5], '100')
			config.set("DATO_1", lista[6], '0')
			config.set("DATO_1", lista[7], '100')

		#Medicion
		i = 0
		GPIO.output(27, 1)

		while i != 1:
			instance = dht11.DHT11(pin=14)
			result = instance.read()
			if not result.is_valid():
				sleep(0.5)
			else:
				tempnow = result.temperature
				humdnow = result.humidity
				i += 1

		GPIO.output(27, 0)

		horanow = strftime("%H:%M:%S")

		config.set('DATO_1', lista[0], datenow)
		config.set('DATO_1', lista[1], horanow)
		config.set('DATO_1', lista[2], str(tempnow))
		config.set('DATO_1', lista[3], str(humdnow))

		#Registra temperatura maxima y minima

		tempmax = config.get('DATO_1', lista[4])
		tempmin = config.get('DATO_1', lista[5])
		humdmax = config.get('DATO_1', lista[6])
		humdmin = config.get('DATO_1', lista[7])

		if tempnow > int(tempmax):
			config.set("DATO_1", lista[4], str(tempnow))

		if tempnow < int(tempmin):
			config.set("DATO_1", lista[5], str(tempnow))

		#Registra humedad maxima y minima

		if humdnow > int(humdmax):
			config.set("DATO_1", lista[6], str(humdnow))

		if humdnow < int(humdmin):
			config.set("DATO_1", lista[7], str(humdnow))

		#Guarda los datos
		with open("/home/pi/Python/TempHumd/medicion.cfg", "w") as f:
			config.write(f)

		#Imprime valores
		"""
		for seccion in config.sections():
			print("\n[%s]" % seccion)
			for item in config.items(seccion):
				print(item[0], ":", item[1])
		"""

		sleep(300)

except KeyboardInterrupt:
	print ("\nCancelado por el usuario")

finally:
	GPIO.cleanup()
	print ("\nHasta luego")
	print ("")
