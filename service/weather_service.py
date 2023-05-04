from data.weather_info import WeatherInfo, convert_dict_to_weather_info

import requests


def get_temperature(lat: float, lng: float):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current_weather=true"
    
    try:
        print(api_url)
        resp =  requests.get(api_url, timeout=2)

        print(resp.status_code)
        
        if resp.status_code >= 400:
            return {"msg": "erro ao fazer a requisição"}
        
        json_resp =  resp.json()
    
        return convert_dict_to_weather_info(json_resp).to_json()
    except BaseException as e:
        print(f"Deu Ruim: {str(e)}")
        
    
    