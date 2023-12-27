import tkinter as tk
from tkinter import ttk
# import customtkinter 
from drive import Drive
from converter import Converter

class CarpoolingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Carpooling Emissions Calculator")
        self.master.geometry("1280x720+100+50")
        self.master.resizable(False, False)

        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack()

        self.create_input_widgets()

    def create_input_widgets(self):
        # labels = [
        #     "Starting Address",
        #     "Ski Resort:",
        #     "Passengers (Driver Excluded)",
        #     "Miles Per Gallon (MPG)"
        # ]

        # for idx, text in enumerate(labels):
        #     # Create a Label widget with the text from the labels list
        #     label = tk.Label(master=self.input_frame, text=text)
        #     # Create an Entry widget
        #     entry = tk.Entry(master=self.input_frame, width=25)
        #     # Use the grid geometry manager to place the Label and
        #     # Entry widgets in the row whose index is idx
        #     label.grid(row=idx, column=0, sticky="e", pady=10)
        #     entry.grid(row=idx, column=1)

        self.address_label = ttk.Label(self.input_frame, text="Starting Address")
        self.address_label.pack()
        self.address_entry = ttk.Entry(self.input_frame)
        self.address_entry.pack()
        
        self.resort_label = ttk.Label(self.input_frame, text="Ski Resort")
        self.resort_label.pack()
       
        self.selected_resort = tk.StringVar()
        self.selected_resort.set("Select a resort")  # Set the initial value

        self.resort_combobox = ttk.Combobox(
            self.input_frame, 
            values=list(Drive.ski_resorts.keys()), 
            height=5,
            textvariable=self.selected_resort 
        )

        self.resort_combobox.pack()

        self.passengers_label = ttk.Label(self.input_frame, text="Number of Passengers (driver excluded)")
        self.passengers_label.pack()
        self.passengers_entry = ttk.Entry(self.input_frame)
        self.passengers_entry.pack()

        self.mpg_label = ttk.Label(self.input_frame, text="Miles per gallon estimation")
        self.mpg_label.pack()
        self.mpg_entry = ttk.Entry(self.input_frame)
        self.mpg_entry.pack()

        self.calculate_button = ttk.Button(self.master, text="Calculate Emissions", command=self.display_results)
        self.calculate_button.pack(pady=10)

    def display_results(self):
        input_address = self.address_entry.get()
        input_resort = self.resort_combobox.get()
        input_passengers = int(self.passengers_entry.get())
        input_mpg = int(self.mpg_entry.get())
        drive = Drive(input_address, input_resort, input_passengers, input_mpg)
        emissions = drive.emissions_saved
        distance = drive.distance
        snow_machine = Converter.snow_machine_hours(emissions)
        beers_brewed = Converter.beers_brewed(emissions)

        # Destroy the input widgets
        self.input_frame.destroy()
        self.calculate_button.destroy()

        # Create a new frame for displaying results
        result_frame = ttk.Frame(self.master)
        result_frame.pack()

        result_text = f"Distance driven: {distance} miles, {emissions} lbs. of CO2 emissions"
        result_label = ttk.Label(result_frame, text=result_text)
        result_label.pack(pady=10)

        result_text_1 = f"{snow_machine}"
        result_label_1 = ttk.Label(result_frame, text=result_text_1)
        result_label_1.pack(pady=10)

        result_text_2 = f"{beers_brewed}"
        result_label_2 = ttk.Label(result_frame, text=result_text_2)
        result_label_2.pack(pady=10)

# Create the main window
root = tk.Tk()

# Instantiate the app
app = CarpoolingApp(root)

# Run the application
root.mainloop()
