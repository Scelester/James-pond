import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)

food_dispenser_servo = gpio.PWM(14,50)

try:
    while True:
        food_dispenser_servo.start(0)
        
        # wait 2 seconds 
        sleep(0.3)

        duty = 1
        while duty <= 20:
            food_dispenser_servo.ChangeDutyCycle(duty)
            print("mooved")
            sleep(0.5)
            duty += 5
        
except KeyboardInterrupt:
    print("programme stopped")
