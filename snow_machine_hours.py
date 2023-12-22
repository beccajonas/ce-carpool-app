from drive import Drive

class Snow_Machine_Hours:
    def __init__(self, ):
        self.drive = Drive()
        self.snow_machine_runtime_metric = self.calculate_snow_machine_runtime_result()
   
    def convert_carbon_to_kwh(self, carbon_emission_pounds):
        # Conversion factor: 1 pound of CO2 = 0.000453592 metric tons
        carbon_emission_metric_tons = carbon_emission_pounds * 0.000453592
        # Given conversion factor: 4.33 × 10^-4 metric tons CO2/kWh
        emission_factor = 4.33e-4
        # Calculate kWh
        kwh = carbon_emission_metric_tons / emission_factor
        return kwh
    
    def calculate_snow_machine_runtime_result(self):
        energy_consumption_rate_kwh_per_hour = 50
        kwh = self.convert_carbon_to_kwh(self.drive.emissions_saved)
        runtime_hours = kwh / energy_consumption_rate_kwh_per_hour
        return runtime_hours
    
    '''
    "If I save a certain amount of carbon emissions during a car ride, 
    how many hours could a snow machine run with that saved energy, 
    considering its energy consumption rate?"
    '''
