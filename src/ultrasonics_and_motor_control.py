import curses
import RPi.GPIO as GPIO
import time
import os

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on. 
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
print("Controls: \n1. UP arrow - move forward\n2. DOWN arrow - move backward\n3. Right arrow - Turn right\n4. Left arrow - Turn left")

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(24,False)
                GPIO.output(23,True)
                GPIO.output(22,False)
                GPIO.output(17,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(24,True)
                GPIO.output(17,False)
                GPIO.output(22,True)
                GPIO.output(23,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(24,True)
                GPIO.output(22,False)
                GPIO.output(23,False)
                GPIO.output(17,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(24,False)
                GPIO.output(22,True)
                GPIO.output(23,True)
                GPIO.output(17,False)
            elif char == 10:
                break

            GPIO.output(24, False)
            GPIO.output(22, False)
            GPIO.output(23, False)
            GPIO.output(17, False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()


#ultrasonics
TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)
while True:
    print("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration = pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    time.sleep(2)