from time import sleep

def start_servo(servo,duty,STATE):
    servo.start(0)
    print("================ servo started =========================")

    servo.ChangeDutyCycle(duty)
    print("Changed duty cycle to initial value :1")
    sleep(1)

    duty = 20
    
    servo.ChangeDutyCycle(duty)
    
    sleep(5)
    duty = 1
    servo.ChangeDutyCycle(duty)
    
    STATE = False