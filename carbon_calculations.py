class Carbon_Calculations:
    def __init__(self, distance, passengers, mpg):
        self.distance = distance
        self.passengers = passengers
        self.mpg = mpg

    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, distance):
        from distance import Distance
        if not isinstance(distance, Distance):
            raise Exception('distance attribute must be instance of Distance')
        self._distance = distance

    @property
    def passengers(self):
        return self._passengers
    
    @passengers.setter
    def passengers(self, passengers):
        if not isinstance(passengers, int):
            raise Exception('Passengers must be a number')
        self._passengers = passengers
        
    @property
    def mpg(self):
        return self._mpg
    
    @mpg.setter
    def mpg(self, mpg):
        if not isinstance(mpg, (int,float)):
            raise Exception('Input must be an number')
        self._mpg = mpg

        
    def calculate_carbon_emssion(self):
        print(self.distance.calculate_distance())
        # pounds_of_carbon = (self.distance / self.mpg) * 19.6
        # print(f”The CO2 emmissions for this drive was {pounds_of_carbon} lbs.“)