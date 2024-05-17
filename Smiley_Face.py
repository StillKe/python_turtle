import cmd
from turtle import *

class TurtleShell(cmd.Cmd):
    # Existing commands...

    def do_smiley(self, arg):
        'Draw a smiley face: SMILEY'
        self.do_circle("50")  # Head
        self.do_position("")  # Move to the position for left eye
        left(90)
        self.do_circle("10")  # Left eye
        right(90)
        self.do_position("30 0")  # Move to the position for right eye
        self.do_circle("10")  # Right eye
        self.do_position("0 -20")  # Move to the position for mouth
        right(90)
        circle(20, 180)  # Draw a semicircle for the mouth

    def do_bounce(self, arg):
        'Animate a bouncing ball: BOUNCE'
        speed(0)
        width(2)
        up()
        goto(-200, 200)
        down()
        for _ in range(100):
            forward(10)
            right(90)
            forward(10)
            right(90)
            forward(10)
            left(90)
            forward(10)
            left(90)
