# Fecha: 07 de febrero de 2026
# Autor: José Armando Sáenz
# Descripción: Programa para indicar la potencia de un motor de CD
# ENA = pin 12, IN1 = pin 16, IN2 = pin 20;
# Se ejecuta en Rapsberry Pi 4B

import RPi.GPIO as GPIO
import time

#Definición de Pines

ENA = 12
IN1 = 16
IN2 = 20

#Nomenclatura a utilizar
GPIO.setmode(GPIO.BCM)

#Habilitando los pines en salida
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

#Definiendo valor de salida
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

#Habilitando el PWM a 1Khz
pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)

print("Programa para control de un motor CD")
print("Para salir del programa presiona las teclas Ctrl + C")

try:
    while True:
        print("Ingresa la potencia con un entero entre 1 - 100")
        valor =  input("")

        if not valor.isdigit():
            print("Es una entrada incorrecta")
            continue

        potencia = int(valor)

        if 0 <= potencia <= 100:
            pwm.ChangeDutyCycle(potencia)
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
            print(f"La potencia ingresada es {potencia}")
        
        else:
            print("La potencia esta fuera de los limites")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa finalizado")

finally:
    pwm.stop()
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.cleanup()