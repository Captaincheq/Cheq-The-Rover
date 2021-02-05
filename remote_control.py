import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
import tkFont


window.mainloop()

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

def forward(event):
    init()
    forward1 = event.char
    sleep_time = 0.030

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
command.title("Cheq_The_Rover")
command.geometry("400x400")
  


turn_left = Button(command, text = "Q", command = key_input, height = 2, width =8 )
turn_left.grid(x=50, y=50) #button position turn right

forward.grid(x=130, y=50) #button position go forward

turn_right = Button(command, text = "E", command = turn_right, height = 2, width =8 )
turn_right.grid(x=190, y=50) #button position turn left

pivot_left= Button(command, text = "A", command = pivot_left, height =2 , width = 6)  
pivot_left.grid(x = 60, y =150 ) #button position reverse Left

reverse= Button(command, text = "D", command = reverse, height =2 , width = 6)  
reverse.grid(x = 123, y =150 ) #button position reverse

pivot_right= Button(command, text = "D", command = pivot_right, height =2 , width = 6)  
pivot_right.grid(x = 183, y = 150) #button position reverse right


command.bind('<KeyPress>', key_input)

Label(window,text='w',fg='blue',font=('Arial',20)).pack(pady=20)
emptylabel

mainloop()