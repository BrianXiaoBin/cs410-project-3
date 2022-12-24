from machine import Pin
import utime

trigger = Pin(14, Pin.OUT) #set the trigger pin as the output
echo = Pin(15, Pin.IN) #set the echo pin as the input
led = Pin(16, Pin.OUT) #configure the led to a gpio
distance = 0

def CheckDistance():
    trigger.low()
    utime.sleep_us(2) #wait time
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0: # measure the duration of the echo
        delaytime = utime.ticks_us()
    while echo.value() == 1:
        receivetime = utime.ticks_us()
        timepassed = receivetime - delaytime
        distance = (timepassed * 0.0343) / 2
        print("The distance from object is ", distance, "cm")

while True:
    CheckDistance()
    if distance < 5:
        led.value(1)
    else:
        led.value(0)