import tkinter as tk
from tkinter import ttk
import customtkinter
from drive import Drive
from converter import Converter

class CarpoolingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Carpooling Emissions Calculator")
        self.master.geometry("1280x720+100+50")
        self.master.resizable(False, False)

        customtkinter.set_appearance_mode("light")

        self.input_frame = customtkinter.CTkFrame(self.master)
        self.input_frame.pack(expand=True, fill='both')

        self.create_input_widgets()

    def create_input_widgets(self):
        self.address_label = customtkinter.CTkLabel(self.input_frame, text="Starting Address")
        self.address_label.pack()
        self.address_entry = customtkinter.CTkEntry(self.input_frame)
        self.address_entry.pack()
        
        self.resort_label = customtkinter.CTkLabel(self.input_frame, text="Ski Resort")
        self.resort_label.pack()

        self.resort_combobox = customtkinter.CTkComboBox(
            self.input_frame,
            values=["Select a Resort"] + list(Drive.ski_resorts.keys())
        )

        self.resort_combobox.set("Select a Resort")
        self.resort_combobox.pack()

        self.passengers_label = customtkinter.CTkLabel(self.input_frame, text="Number of Passengers (driver excluded)")
        self.passengers_label.pack()
        self.passengers_entry = customtkinter.CTkEntry(self.input_frame)
        self.passengers_entry.pack()

        self.mpg_label = customtkinter.CTkLabel(self.input_frame, text="Miles per gallon estimation")
        self.mpg_label.pack()
        self.mpg_entry = customtkinter.CTkEntry(self.input_frame)
        self.mpg_entry.pack()

        self.calculate_button = customtkinter.CTkButton(self.input_frame, text="Calculate Emissions", command=self.validate_and_display_results)
        self.calculate_button.pack(pady=10)

    def validate_and_display_results(self):
        try:
            input_address = self.address_entry.get()
            input_resort = self.resort_combobox.get()
            input_passengers = self.passengers_entry.get()
            input_mpg = self.mpg_entry.get()

            drive = Drive(input_address, input_resort, input_passengers, input_mpg)
            print(input_address)
            print(input_resort)
            print(type(input_passengers))
            print(type(input_mpg))

            # Display results only if validations pass
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

        except ValueError as ve:
            # Handling specific ValueError from the Drive class
            tk.messagebox.showerror("Error", str(ve))

# Create the main window
root = tk.Tk()

# Instantiate the app
app = CarpoolingApp(root)

# Run the application
root.mainloop()
