import RPi.GPIO as GPIO
import time

trig=20
echo=21

def init_hcsr():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)

def read_distance():
    GPIO.output(trig, GPIO.LOW)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.HIGH)

    while not (GPIO.input(echo) == 1):
        pass
    start = time.time()

    while not (GPIO.input(echo) == 0):
        pass
    end = time.time()

    distance = round((end - start) * 343 / 2 * 100, 2)
    print("distance:{0}cm".format(distance))
    return distance

init_hcsr()
while Ture:
    a=read_distance()
    time.sleep(0.1)

GPIO.cleanup()
    