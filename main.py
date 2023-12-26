from drive import Drive
from converter import Converter

if __name__ == '__main__':
    '''
    Get start and end points to begin app
    '''


input_origin = input('Enter your starting address (Address Line 1, City, State) >> ')
input_name = input('Enter the Utah Ski Resort you plan to visit >> ')
input_passengers = int(input('Enter the number of passengers in your car >> '))
input_mpg = float(input('What is your gas mileage? An estimated number is fine >> '))


drive = Drive(input_origin, input_name, input_passengers, input_mpg)
emissions = drive.emissions_saved


print(f"Distance driven: {drive.distance} miles")
print(f"Emissions released: {drive.ride_emissions} lbs of CO2")
print(f"By carpooling, you are saving: {drive.emissions_saved} lbs of CO2")
print(Converter.snow_machine_hours(emissions))
print(Converter.beers_brewed(emissions))