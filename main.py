from drive import Drive

if __name__ == '__main__':
    '''
    Get start and end points to begin app
    '''


input_origin = input('Enter your starting address >> ')
input_name = input('Enter the Utah Ski Resort you plan to visit >> ')
input_passengers = int(input('Enter the number of passengers included in your carpool >> '))
input_mpg = float(input('What is your gas mileage? An estimated number is fine >> '))


drive = Drive(input_origin, input_name, input_passengers, input_mpg)
print(drive.distance)
