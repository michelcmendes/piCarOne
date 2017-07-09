import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from sensor import distance


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(16, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def reverse(tf):
    gpio.output(16, False)
    gpio.output(18, True)
    gpio.output(22, False)
    gpio.output(24, True)
    time.sleep(tf)

def forward(tf):
    gpio.output(16, True)
    gpio.output(18, False)
    gpio.output(22, True)
    gpio.output(24, False)
    time.sleep(tf)

def turn_right(tf):
    gpio.output(16, True)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(24, True)
    time.sleep(tf)

def turn_left(tf):
    gpio.output(16, False)
    gpio.output(18, True)
    gpio.output(22, True)
    gpio.output(24, False)
    time.sleep(tf)

def stop(tf):
    gpio.output(16, False)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()

def key_input(event):
    init()
    print "Key:", event.char
    key_press = event.char
    sleep_time = 0.060

    if key_press.lower() == "w":
        forward(sleep_time)
    elif key_press.lower() == "s":
        reverse(sleep_time)
    elif key_press.lower() == "a":
        turn_left(sleep_time)
    elif key_press.lower() == "d":
        turn_right(sleep_time)
    elif key_press.lower() == "p":
        stop(sleep_time)
    else:
        pass

    curDis = distance("cm")
    print("Distance:", curDis)

    if curDis <15:
        init()
        reverse(0.5)

command = tk.Tk()
command.bind('<keypress>', key_input)
command.mainloop()
