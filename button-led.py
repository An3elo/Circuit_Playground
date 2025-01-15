# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

myButtonB = digitalio.DigitalInOut(board.BUTTON_B)
myButtonB.direction = digitalio.Direction.INPUT
myButtonB.pull = digitalio.Pull.DOWN

while True:
    led.value = myButtonB.value
    print(myButtonB.value)
    time.sleep(0.5)
