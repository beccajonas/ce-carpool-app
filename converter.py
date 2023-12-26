class Converter:
    def snow_machine_hours(emissions):
        carbon_emission_metric_tons = emissions * 0.000453592
        emission_factor = 4.33e-4
        kwh = carbon_emission_metric_tons / emission_factor
        snow_machine_runtime = kwh / 50 
        total_minutes = int(snow_machine_runtime * 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        if hours == 0:
            return f"With the amount of carbon emissions you saved by carpooling, you have saved enough energy to run a snow machine for {minutes} minutes."
        else:
            return f"With the amount of carbon emissions you saved by carpooling, you have saved enough energy to run a snow machine for {hours} hours and {minutes} minutes."
    
    def beers_brewed(emissions):
        carbon_emission_metric_tons = emissions * 0.000453592
        emission_factor = 4.33e-4
        kwh = carbon_emission_metric_tons / emission_factor
        brewery_runtime = kwh / 50
        # Assuming a 12oz pour and a 31-gallon barrel
        ounces_per_beer = 12
        gallons_per_barrel = 31
        beers_in_barrel = (gallons_per_barrel * 128) / ounces_per_beer
        # Calculate the number of beers brewed
        beers_brewed_result = round(brewery_runtime * beers_in_barrel)
        return f"With the amount of carbon emissions you saved by carpooling, you have saved enough energy to brew {beers_brewed_result} beers."
        
    def trees_planted(emission_amount):
        pass
