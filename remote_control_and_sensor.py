import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from sensor import distance
import random

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

def check_front():
    init()
    dist = distance()

    if dist < 15:
        print('Too close,',dist)
        init()
        reverse(2)
        dist = distance()
        if dist < 15:
            print('Too close,',dist)
            init()
            pivot_left()
            init()
            reverse(2)
            dist = distance()
            if dist < 15:
                print('Too close, give up',dist)
                sys.exit()

def autonomy():
    tf = 0.030
    x = random.randrange(0,4)

    if x == 0:
        for y in range(30):
            check_front()
            init()
            forward(tf)
    elif x ==1:
        for y in range(30):
            check_front()
            init()
            pivot_left(tf)
    elif x == 2:
        for y in range(30):
            check_front()
            init()
            turn_right(tf)
    elif x == 3:
        for y in range(30):
            check_front()
            init()
            turn_left(tf)

for z range(10):
    autonomy()
