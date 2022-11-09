import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)

food_dispenser_servo = gpio.PWM(14,50)

duty = 5
x = 0

try:
    while True:
        food_dispenser_servo.start(0)
        sleep(0.5)
        if x < 20:
            food_dispenser_servo.ChangeDutyCycle(duty)
        else:
            # food_dispenser_servo.changeDutyCycle(0)
            food_dispenser_servo.stop()
            gpio.cleanup()

            print("loop broke")
            break

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("some error") 

finally:
   print("clean up") 
   GPIO.cleanup() # cleanup all GPIO 