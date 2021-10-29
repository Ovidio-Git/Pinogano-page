import machine                           # Importamos la libreria machine para leer el sensor y usar el modo sleep
import socket                          	 # Importamos la libreria de socket para poder enviar datos al servidor
from time import time, sleep             # Importamos la libreria time para realizar delays



def potencia():
	sumatoria, n    = 0, 0				    # Inicializamos las variables en 0
	irms, corriente = 0, 0	             		    # Inicializamos las variables en 0
	adc    = machine.ADC(0)                             # Leemos el conversor analogo digital 
	tiempo = time()					    # Guardamos el tiempo que lleva el programa ejecutandose
	while (time() - tiempo) < 0.5:                      # Duración 0.5 segundos(Aprox. 30 ciclos de 60Hz)
		voltaje   = adc.read() * (1/1023.0)         # voltaje del sensor
		corriente = voltaje*30.0		    # Corriente del sensor = Voltaje del sensor * (30A/1V)
		sumatoria = sumatoria+(corriente*corriente) # Sumatoria de Cuadrados para calcualr corriente irms
		n = n+1										# Llevamos conteo del numero de ciclos realizados para luego calcular la corriente irms
		sleep(0.1)									# Ejecutamos un diley de 100 ms
	sumatoria = sumatoria * 2	     # Para compensar los cuadrados de los semiciclos negativos multiplicamos la corriente por 2.
	corriente = (sumatoria/n)**(1/2)     # Ecuación del RMS
	irms=corriente 	     		     # Corriente eficaz (A)
	potence=irms*110.0  		     # Potencia = Coriente * Voltage (W)
	print ("corriente recolectada: ", corriente," A")   # Imprimimos el valor de la corriente recolectada
	print ("Potencia  recolectada: ", potence," W\n\r") # Imprimimos el valor de la potencia recolectada
	return potence



def request(url, sensor):
	addr = socket.getaddrinfo(url, 80)[0][-1]  # Extraemos la direccion del host al que deseamos conectarnos
	s = socket.socket()
	s.connect(addr)                            # Nos conectamos al host donde se almacenara la informacion
	s.send(bytes('POST /metrics/%s HTTP/1.1\r\nContent-Type: multipart/form-data; boundary=---011000010111000001101001\r\nHost: pinogano2.mooo.com\r\n\r\n'% (sensor), 'utf8')) # Enviamos una preticion POST al host con el valor del sensor
	data = s.recv(150)                         # Recibimos la respuesta del servidor al recivir la peticion enviada
	print(str(data, 'utf8'), end='')           # Imprimimos la respuesta recivida del servidor 



def sleep_mode(reset_time):
	rtc = machine.RTC() 							# Iniciamos la variable rtc con el metodo Real Time Clock
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP) 			# Configuiramos el modo sleep
	rtc.alarm(rtc.ALARM0, reset_time)					# Definimos en cuanto timepo queremos que se resete el modulo 



def current():
	pin = machine.Pin(2, machine.Pin.OUT)					# Iniciamos la variable pin con el metodo Pin.Out para poder contolar si el pin se enciende o se apaga
	pin.off()								# Encendemos el pin cada que se este realize la lectura del sensor
	data, value = 0, 0							# Inicializamos las variables en 0
	sleep(0.5)				    				# Ejecutamos un delay  antes de empezar el proceso
	for _ in range(9):							# Realizamos El proceso de lectura 9 veces
		value += potencia()						# Almacenamos el valor leido de la potencia
	if value > data:							# Verificamos que hayamos obtenido datos
		data = value / 9						# Sacamos el promedio de la potencia obtenida
	print("Potencia Promedio:", data,"W")				        # Imprimimos el valor de la potencia promedio
	request("pinogano2.mooo.com", str(data))    				# Enviamos la informacion al servidor
	print("\n\rHasta Luego  T.T")               				# Imprimimos un mensaje de que el modo sleep se ejecutara
	machine.deepsleep()							# Ponemos el microcontrolador en modo sleep



def run():
	if machine.reset_cause() == machine.DEEPSLEEP_RESET: 			 # Hacemos un cast a la variable DEEPSLEEP_RESET para saber cual fue el motivo del reset del micro
		print('\n\rDespertando xD ...')				 	 # Imprimimos un mensaje cuando el motivo del reset fue por el modo sleep
	else:
		print('\n\rMe resetearon, Chau T-T ')		     		 # Imprimimos un mensaje cuando el motivo del reset fue por presionar el boton externo
	sleep_mode(300000)							 # Le asignamos el tiempo de cada cuando deseamos que el micro ingrese a modo sleep en este caso cada 5 minutos
	current()								 # leemos el valor de la potencia detectada por el sensor



if __name__ == '__main__':
	run()
