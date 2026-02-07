import RPi.GPIO as GPIO #Librería para el GPIO
import time #Librería para las pausas

LED_PIN = 12 #Pin donde esta el led

GPIO.setmode(GPIO.BCM) #Numeración BCM
GPIO.setup(LED_PIN, GPIO.OUT) #Pin 12 como salida

pwm = GPIO.PWM(LED_PIN, 1000) #Periodo de 1 KHz
pwm.start(0) #Inicia el puerto en estado bajo

try:
    while True:
        #Rutina para incrementar la intensidad del LED
        for duty in range(0,101,5):
            pwm.ChangeDutyCycle(duty) 
            print(f"Brillo: {duty}%")
            time.sleep(0.5)
        
        #Rutina para bajar la intensidad del LED
        for duty in range(100,-1,-5):
            pwm.ChangeDutyCycle(duty)
            print(f"Brillo: {duty}%")
            time.sleep(0.5)
except KeyboardInterrupt:
    print("Programa detenido")

finally: 
    pwm.stop()
    GPIO.cleanup()
