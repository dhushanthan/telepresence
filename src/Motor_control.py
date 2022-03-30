import curses
import RPi.GPIO as GPIO
import pygame

pygame.init()
display = pygame.display.set_mode((300, 300))

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
    run = True
    while run:   
        for event in pygame.event.get():
            if event.type == pygame.K_END:
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    GPIO.output(24,False)
                    GPIO.output(23,True)
                    GPIO.output(22,False)
                    GPIO.output(17,True)
                if event.key == pygame.K_DOWN:
                    GPIO.output(24,True)
                    GPIO.output(17,False)
                    GPIO.output(22,True)
                    GPIO.output(23,False)
                if event.key == pygame.K_RIGHT:
                    GPIO.output(24,False)
                    GPIO.output(22,True)
                    GPIO.output(23,True)
                    GPIO.output(17,False)
                if event.key == pygame.K_LEFT:
                    GPIO.output(24,True)
                    GPIO.output(22,False)
                    GPIO.output(23,False)
                    GPIO.output(17,True)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    GPIO.output(24, False)
                    GPIO.output(23, False)
                    GPIO.output(22, False)
                    GPIO.output(17, False)


             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
