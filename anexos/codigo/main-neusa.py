# ---------------------------------------------------------------
# Nodo de monitoreo hidrico - Cliente MQTT
# Red Sabana Centro - Actividad de refuerzo #2.3
#
# Publica cinco variables ambientales hacia el broker MQTT
# siguiendo el esquema de topicos sabanacentro/<punto>/<variable>
# ---------------------------------------------------------------

from cli import *
from gui import *
import json
import mqttclient
import random
from time import *

# --- Configuracion del nodo -------------------------------------

BROKER    = "192.168.1.102"
USUARIO   = "admin"
CLAVE     = "sabana123"
PUNTO     = "neusa"          
QOS       = "0"
INTERVALO = 10000            # ms entre ciclos de publicacion

# --- Rangos de las variables ------------------------------------
# Basados en promedios climatologicos IDEAM para Sabana Centro
# y calculo barometrico estandar para la altitud del sitio.

TEMP_AMBIENTE_MIN, TEMP_AMBIENTE_MAX = 9.0, 20.0
HUMEDAD_MIN,       HUMEDAD_MAX       = 85.0, 90.0
TEMP_AGUA_MIN,     TEMP_AGUA_MAX     = 8.0, 13.0
LUZ_MIN,           LUZ_MAX           = 0.0, 100000.0
PRESION_KPA = 70.0           # ~3.000 msnm (Neusa)

# --- Callbacks --------------------------------------------------
# Sin CLI.exit(): el nodo publica de forma autonoma y no debe
# terminar la ejecucion tras cada operacion.

def on_connect(status, msg, packet):
	print ("[CONNECT] " + str(status) + ": " + str(msg))

def on_publish(status, msg, packet):
	print ("[PUBLISH] " + str(status) + ": " + str(msg))

def on_disconnect(status, msg, packet):
	print ("[DISCONNECT] " + str(status) + ": " + str(msg))

# --- Logica del nodo --------------------------------------------

def valorAleatorio(minimo, maximo):
	return round(random.uniform(minimo, maximo), 2)

def topico(variable):
	return "sabanacentro/" + PUNTO + "/" + variable

def publicarLectura():
	mqttclient.publish(topico("temp_ambiente"),
		str(valorAleatorio(TEMP_AMBIENTE_MIN, TEMP_AMBIENTE_MAX)), QOS)
	delay(500)

	mqttclient.publish(topico("humedad"),
		str(valorAleatorio(HUMEDAD_MIN, HUMEDAD_MAX)), QOS)
	delay(500)

	mqttclient.publish(topico("temp_agua"),
		str(valorAleatorio(TEMP_AGUA_MIN, TEMP_AGUA_MAX)), QOS)
	delay(500)

	mqttclient.publish(topico("luz"),
		str(valorAleatorio(LUZ_MIN, LUZ_MAX)), QOS)
	delay(500)

	mqttclient.publish(topico("presion"),
		str(PRESION_KPA), QOS)

def main():
	mqttclient.init()
	mqttclient.onConnect(on_connect)
	mqttclient.onPublish(on_publish)
	mqttclient.onDisconnect(on_disconnect)

	mqttclient.connect(BROKER, USUARIO, CLAVE)
	delay(5000)   # margen para completar CONNECT / CONNACK

	while True:
		publicarLectura()
		delay(INTERVALO)

if __name__ == "__main__":
	main()