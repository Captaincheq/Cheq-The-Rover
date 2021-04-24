import RPi.GPIO as gpio
import time
import sys
#import Tkinter as tk
gpio.setwarnings(False)
#command = tk.Tk()
class Motor():
	def __init__(self,In1A,In2A,In1B,In2B):
	    self.In1A = In1A
	    self.In2A = In2A
	    self.In1B = In1B
	    self.In2B = In2B
	    gpio.setmode(gpio.BOARD)
	    gpio.setup(self.In1A, gpio.OUT)
	    gpio.setup(self.In2A, gpio.OUT)
	    gpio.setup(self.In1B, gpio.OUT)
	    gpio.setup(self.In2B, gpio.OUT)

	def forward(tf):
	    gpio.output(In1A, True)
	    gpio.output(In2A, False)
	    gpio.output(In1B, False)
	    gpio.output(In2B, False)
	    time.sleep(tf)
	    gpio.cleanup()

	def reverse(tf):
	    gpio.output(In1A, False)
	    gpio.output(In2A, True)
	    gpio.output(In1B, False)
	    gpio.output(In2B, False)
	    time.sleep(tf)
	    gpio.cleanup()

	def turn_left(tf):
	    gpio.output(In1A, True)
	    gpio.output(In2A, False)
	    gpio.output(In1B, True)
	    gpio.output(In2B, False)
	    time.sleep(tf)
	    gpio.cleanup()

	def turn_right(tf):
	    gpio.output(In1A, True)
	    gpio.output(In2A, False)
	    gpio.output(In1B, False)
	    gpio.output(In2B, True)
	    time.sleep(tf)
	    gpio.cleanup()

	def pivot_left(tf):
	    gpio.output(In1A, False)
	    gpio.output(In2A, True)
	    gpio.output(In1B, True)
	    gpio.output(In2B, False)
	    time.sleep(tf)
	    gpio.cleanup()

	def pivot_right(tf):
	    gpio.output(In1A, False)
	    gpio.output(In2A, True)
	    gpio.output(In1B, False)
	    gpio.output(In2B, True)
	    time.sleep(tf)
	    gpio.cleanup()


	def key_input(event):
	    init()
	    print('Key:', event.char)
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
	        pivot_left(sleep_time)
	    elif key_press.lower() == 'd':
	        pivot_right(sleep_time)
	    else:
	        gpio.cleanup()


	command.bind('<KeyPress>', key_input)
	command.mainloop()
if __name__ == '__main__':
	motor = Motor(32,36,38,40)
	main()