#importing required libraries
import tkinter as tk
import RPi.GPIO as GPIO

# Pin numbers for LED'S
LED_PINS = {
    "Red": 17,    
    "Green": 18,
    "Blue": 27,
}

# Initializing GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# setting the color of the LED's
def set_led_color(color):
    for pin in LED_PINS.values():
        GPIO.output(pin, GPIO.LOW)  
    GPIO.output(LED_PINS[color], GPIO.HIGH)  

#creating the window
root = tk.Tk()
root.title("LED Controller")
root.geometry("300x200")  

# Creating the label
label = tk.Label(root, text="Select the color of LED: ", font=("Arial", 20))
label.pack(pady=20)

# handling buttons
def button_click(color):
    set_led_color(color)

# loop for each color led light
for color in LED_PINS.keys():
    button = tk.Button(root, text=color, command=lambda c=color: button_click(c))
    button.pack(pady=15)

#exiting 
exit_button = tk.Button(root, text="Exiting", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()

# cleang the GPIO after the program ends
GPIO.cleanup()