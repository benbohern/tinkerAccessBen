import time
import RPi.GPIO as GPIO

channel = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup (channel, GPIO.IN,  GPIO.PUD_DOWN)

if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')

while GPIO.input(channel) == GPIO.LOW:
    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things

print("went high ")

