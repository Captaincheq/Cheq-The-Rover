import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(32, gpio.OUT)
    gpio.setup(36, gpio.OUT)
    gpio.setup(38, gpio.OUT)
    gpio.setup(40, gpio.OUT)

def forward(tf):
    gpio.output(32, True)
    gpio.output(36, False)
    gpio.output(38, False)
    gpio.output(40, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    gpio.output(32, False)
    gpio.output(36, True)
    gpio.output(38, False)
    gpio.output(40, False)
    time.sleep(tf)
    gpio.cleanup()


def turn_left(tf):
    gpio.output(32, True)
    gpio.output(36, False)
    gpio.output(38, True)
    gpio.output(40, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    gpio.output(32, True)
    gpio.output(36, False)
    gpio.output(38, False)
    gpio.output(40, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    gpio.output(32, False)
    gpio.output(36, True)
    gpio.output(38, True)
    gpio.output(40, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    gpio.output(32, False)
    gpio.output(36, True)
    gpio.output(38, False)
    gpio.output(40, True)
    time.sleep(tf)
    gpio.cleanup()


def key_input(event):
    init()
    print 'Key:',event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'q':
        turn_left(sleep_time)
    elif key_press.lower() == 'e':
        turn_right(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    else:
        gpio.cleanup()


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()