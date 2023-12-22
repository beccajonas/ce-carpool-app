from drive import Drive
from snow_machine_hours import Snow_Machine_Hours

if __name__ == '__main__':
    '''
    Get start and end points to begin app
    '''


input_origin = input('Enter your starting address >> ')
input_name = input('Enter the Utah Ski Resort you plan to visit >> ')
input_passengers = int(input('Enter the number of passengers included in your carpool not including the driver >> '))
input_mpg = float(input('What is your gas mileage? An estimated number is fine >> '))


drive = Drive(input_origin, input_name, input_passengers, input_mpg)

print(f"Your driving distance is: {drive.distance} miles")
print(f"Your drives emissions are: {drive.ride_emissions} lbs of CO2")
print(f"By carpooling, you are saving: {drive.emissions_saved} lbs of CO2")
