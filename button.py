from gpiozero import Button

button = Button (16)

button.wait_for_press()

print ("you pushed me")
