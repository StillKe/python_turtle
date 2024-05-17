import tkinter as tk
from tkinter import messagebox
from TurtleShell import TurtleShell

class TurtleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Turtle Shell")
        self.geometry("500x500")

        self.instructions = tk.Label(self, text=(
            "Enter commands in the input box and click 'Execute' to control the turtle.\n"
            "Available commands:\n"
            "FORWARD <distance>\nRIGHT <angle>\nLEFT <angle>\nGOTO <x> <y>\n"
            "HOME\nCIRCLE <radius>\nPOSITION\nHEADING\nCOLOR <color>\n"
            "UNDO\nRESET\nBYE"
        ), justify=tk.LEFT)
        self.instructions.pack(pady=10)

        self.command_entry = tk.Entry(self)
        self.command_entry.pack(pady=10)

        self.execute_button = tk.Button(self, text="Execute", command=self.execute_command)
        self.execute_button.pack(pady=5)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_turtle)
        self.reset_button.pack(pady=5)

        self.help_button = tk.Button(self, text="Help", command=self.show_help)
        self.help_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=5)

        self.shell = TurtleShell()

    def execute_command(self):
        command = self.command_entry.get()
        # Here, you would process the command to control the turtle
        # For example, self.shell.screen.forward(100) for moving forward
        self.command_entry.delete(0, tk.END)

    def reset_turtle(self):
        # Here, you would reset the turtle graphics
        pass

    def show_help(self):
        messagebox.showinfo("Help", (
            "Enter commands in the input box and click 'Execute' to control the turtle.\n\n"
            "Available commands:\n"
            "- FORWARD <distance>: Move the turtle forward by the specified distance.\n"
            "- RIGHT <angle>: Turn turtle right by the given number of degrees.\n"
            "- LEFT <angle>: Turn turtle left by the given number of degrees.\n"
            "- GOTO <x> <y>: Move turtle to an absolute position with changing orientation.\n"
            "- HOME: Return turtle to the home position.\n"
            "- CIRCLE <radius>: Draw a circle with the given radius.\n"
            "- POSITION: Print the current turtle position.\n"
            "- HEADING: Print the current turtle heading in degrees.\n"
            "- COLOR <color>: Set the color of the turtle.\n"
            "- UNDO: Undo the last turtle action(s).\n"
            "- RESET: Clear the screen and return turtle to the center.\n"
            "- BYE: Stop and exit the application."
        ))

    def quit(self):
        self.shell.close()  # Close the turtle graphics window and environment
        self.destroy()  # Close the Tkinter application