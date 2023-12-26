import tkinter as tk
from drive import Drive
from converter import Converter

class CarpoolingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Carpooling Emissions Calculator")

# Create the main window
root = tk.Tk()

# Instantiate the app
app = CarpoolingApp(root)

# Run the application
root.mainloop()
