from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

win = Tk()
win.title("LED TOGGLE");
font_settings = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

Red_Led = LED(16)
Yellow_Led = LED(20)
Green_Led = LED(21)
value = IntVar()

def led_toggle():
    var = value.get()
    if var == 1:
       Red_Led.on()
       Yellow_Led.off()
       Green_Led.off()
        
    elif var == 2:
        Red_Led.off()
        Yellow_Led.on()
        Green_Led.off()

    elif var == 3:
        Red_Led.off()
        Yellow_Led.off()
        Green_Led.on()
    else:
        Red_Led.off()
        Yellow_Led.off()
        Green_Led.off()

def Close():
    GPIO.cleanup()
    win.destroy()
    


red_button = Radiobutton( win, text = "RED LED", font = font_settings, variable = value, value = 1, command = led_toggle, height = 1, width = 8)
red_button.grid( row = 1, column = 0)

yellow_button = Radiobutton( win, text = "YELLOW LED", font = font_settings, variable = value, value= 2, command = led_toggle, height = 1, width = 8)
yellow_button.grid( row = 1, column = 1)

green_button = Radiobutton( win, text = "GREEN LED", font = font_settings, variable = value, value = 3, command = led_toggle, height = 1, width = 8)
green_button.grid( row = 1, column = 2)

close_button = Radiobutton( win, text = "EXIT", font = font_settings,command = Close, height = 1, width = 5)
green_button.grid( row = 2, column = 3)


win.mainloop()



    




