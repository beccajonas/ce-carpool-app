from googlemaps import Client
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

class Distance:
    ski_resorts = {
        "Beaver Mountain": "40000 East, US-89, Garden City, UT 84028",
        "Cherry Peak": "3200 E 11000 N, Richmond, UT 84333",
        "Powder Mountain": "6965 E Powder Mountain Rd, Eden, UT 84310",
        "Nordic Valley": "3567 Nordic Valley Way, Eden, UT 84310",
        "Snowbasin": "925 E. Snowbasin Road Huntsville, Utah 84317",
        "Park City": "1355 Lowell Ave, Park City, UT 84060",
        "Woodward": "3863 Kilby Rd, Park City, UT 84098",
        "Brighton": "8302 S Brighton Loop Rd, Brighton, UT 84121",
        "Deer Valley": "2250 Deer Valley Dr S, Park City, UT 84060",
        "Solitude": "12000 Big Cottonwood Canyon Rd, Solitude, UT 84121",
        "Alta": "10300 Little Cottonwood Rd, Alta, UT 84092",
        "Snowbird": "9385 Snowbird Center Trail, Snowbird, UT 84092",
        "Sundance": "8841 Alpine Loop Scenic Byway, Sundance, UT 84604",
        "Brian Head": "329 UT-143, Brian Head, UT 84719",
        "Eagle Point": "150 S W Village Cir, Beaver, UT 84713"
    }


    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        if not isinstance(origin, str):
            raise Exception('Origin must be specified as a string')
        self._origin = origin

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        if destination not in self.ski_resorts:
            raise Exception("That’s not a Utah Ski Resort... Try again")
        self._destination = self.ski_resorts[destination]

    def calculate_distance(self):
        gmaps = Client(key=api_key)

        try:
            directions_result = gmaps.directions(self.origin, self.destination, mode="driving")
            distance = directions_result[0]['legs'][0]['distance']['text']
            print(f"The driving distance between {self.origin} and {self.destination} is: {distance}")
        except Exception as e:
            print(f"Error calculating distance: {e}")