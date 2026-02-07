import RPi.GPIO as GPIO #Librería de los puertos digitales
import time #Librería para pausas en el código

ENA = 6
IN1 = 12 #Número de pin donde esta conectado el led
IN2 = 13 #Número de pin donde esta conectado el led

GPIO.setmode(GPIO.BCM) #Escogiendo numeración BCM para seleccionar los pines
GPIO.setup(ENA, GPIO.OUT) #Estableciendo el LED_PIN como salida
GPIO.setup(IN1, GPIO.OUT) #Estableciendo el LED_PIN como salida
GPIO.setup(IN2, GPIO.OUT) #Estableciendo el LED_PIN como salida

GPIO.output(ENA, GPIO.HIGH) #Estableciendo LED_PIN en estado alto
GPIO.output(IN1, GPIO.HIGH) #Estableciendo LED_PIN en estado alto
GPIO.output(IN2, GPIO.HIGH) #Estableciendo LED_PIN en estado alto
try:
    while True:
        time.sleep(1) #Pausa de 1 segundo

except KeyboardInterrupt:
    print("Programa detenido") #Mensaje para el usuario

finally:
    GPIO.cleanup() #Se liberan los recursos del GPIO