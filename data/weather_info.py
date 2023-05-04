class WeatherInfo:
    def __init__(self, latitude, longitude, current_temperature) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.current_temperature = current_temperature
        
        
    def to_json(self):
        return {"lat": self.latitude, "lng": self.longitude, "temperature": self.current_temperature}


def convert_dict_to_weather_info(api_resp: dict) -> WeatherInfo :
    current_weather =  api_resp["current_weather"]
    return WeatherInfo(
        api_resp["latitude"],
        api_resp["longitude"],
        current_weather["temperature"]
    )