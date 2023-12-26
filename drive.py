from googlemaps import Client
from dotenv import load_dotenv
import os
import re

load_dotenv()
api_key = os.getenv('API_KEY')

class Drive:
    ski_resorts = {
        "Beaver Mountain": "40000 East, US-89, Garden City, UT 84028", # 1
        "Cherry Peak": "3200 E 11000 N, Richmond, UT 84333", # 2
        "Powder Mountain": "6965 E Powder Mountain Rd, Eden, UT 84310", # 3
        "Nordic Valley": "3567 Nordic Valley Way, Eden, UT 84310", # 4
        "Snowbasin": "925 E. Snowbasin Road Huntsville, Utah 84317", #5
        "Park City": "1355 Lowell Ave, Park City, UT 84060", #6 
        "Woodward": "3863 Kilby Rd, Park City, UT 84098", #7
        "Brighton": "8302 S Brighton Loop Rd, Brighton, UT 84121", #8
        "Deer Valley": "2250 Deer Valley Dr S, Park City, UT 84060", #9
        "Solitude": "12000 Big Cottonwood Canyon Rd, Solitude, UT 84121", #10
        "Alta": "10300 Little Cottonwood Rd, Alta, UT 84092", #11
        "Snowbird": "9385 Snowbird Center Trail, Snowbird, UT 84092", #12
        "Sundance": "8841 Alpine Loop Scenic Byway, Sundance, UT 84604", #13
        "Brian Head": "329 UT-143, Brian Head, UT 84719", #14
        "Eagle Point": "150 S W Village Cir, Beaver, UT 84713" #15
    }


    def __init__(self, start, end, passengers, mpg):
        self.start = start
        self.end = end
        self.passengers = passengers
        self.mpg = mpg

        self.distance = self.calculate_distance()
        self.ride_emissions = self.calculate_ride_emissions()
        self.emissions_saved = self.calculate_emissions_saved()

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        if not isinstance(start, str):
            raise Exception('Origin must be specified as a string')
        self._start = start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        if end not in self.ski_resorts:
            raise Exception("That’s not a Utah Ski Resort... Try again")
        self._end = self.ski_resorts[end]
    
    @property
    def passengers(self):
        return self._passengers
    
    @passengers.setter
    def passengers(self, passengers):
        if not isinstance(passengers, int):
            raise Exception("Please enter an integer")
        self._passengers = passengers

    @property
    def mpg(self):
        return self._mpg

    @mpg.setter
    def mpg(self, mpg):
        if not isinstance(mpg, int):
            raise Exception("Pleae enter an integer")
        self._mpg = mpg

    def calculate_distance(self):
        gmaps = Client(key=api_key)

        try:
            directions_result = gmaps.directions(self.start, self.end, mode="driving")
            distance_text = directions_result[0]['legs'][0]['distance']['text']

            # Extract the numeric part from the distance string using regular expressions
            numeric_distance = float(re.search(r'\d+\.\d+', distance_text).group())

            return numeric_distance
        except Exception as e:
            print(f"Error calculating distance: {e}")

    def calculate_ride_emissions(self):
        ride_emissions = round((self.distance / self.mpg) * 19.6, 1)
        # 19.6 represents the emissions factor (generalized estimation for average car)
        return ride_emissions

    def calculate_emissions_saved(self):
        emissions_if_not_carpooling = self.ride_emissions * (self.passengers + 1)
        # if each person drove alone, they'd use emissions_if_not_carpooling
        emissions_saved_by_carpooling = round((emissions_if_not_carpooling - self.passengers), 2)
        # since they rode together, the emissions they saved is the total 
        return emissions_saved_by_carpooling
    