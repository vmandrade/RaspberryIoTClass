import RPi.GPIO as GPIO #Librería de los puertos digitales
import time #Librería para pausas en el código

LED_PIN = 12 #Número de pin donde esta conectado el led

GPIO.setmode(GPIO.BCM) #Escogiendo numeración BCM para seleccionar los pines
GPIO.setup(LED_PIN, GPIO.OUT) #Estableciendo el LED_PIN como salida

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) #Estableciendo LED_PIN en estado alto
        print("ENCENDIENDO EL LED") #Mensaje para el usuario
        time.sleep(1) #Pausa de 1 segundo

        GPIO.output(LED_PIN, GPIO.LOW) #Estableciendo LED_PIN en estado bajo
        print("Apagando el LED") #Mensaje para el usuario
        time.sleep(1) #Pausa de 1 segundo

except KeyboardInterrupt:
    print("Programa detenido") #Mensaje para el usuario

finally:
    GPIO.cleanup() #Se liberan los recursos del GPIO