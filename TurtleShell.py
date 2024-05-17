from turtle import Screen, bye

class TurtleShell:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=500, height=500)
        self.screen.title("Turtle Graphics")

    def close(self):
        self.screen.bye()