import requests
from API import api_key

def validate_city_name(city_name):
    if not city_name.strip():
        return False, "Пожалуйста, введите название города"
    return True, ""

def validate_coordinates(lat, lon):
    try:
        lat = float(lat)
        lon = float(lon)
        if not (-90 <= lat <= 90):
            return False, "Широта должна быть в диапазоне от -90 до 90"
        if not (-180 <= lon <= 180):
            return False, "Долгота должна быть в диапазоне от -180 до 180"
        return True, ""
    except ValueError:
        return False, "Широта и долгота должны быть числами"

def get_weather_by_city(city_name):
    try:
        location_url = f'https://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city_name}'
        location_response = requests.get(location_url, timeout=10)
        location_response.raise_for_status()

        location_data = location_response.json()
        if not location_data:
            raise ValueError("Город не найден")

        location_key = location_data[0]['Key']

        weather_url = f'https://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}&details=true'
        weather_response = requests.get(weather_url, timeout=10)
        weather_response.raise_for_status()

        weather_data = weather_response.json()
        if not weather_data:
            raise ValueError("Нет данных о погоде")

        weather_information = {
            "Время наблюдения": weather_data[0]['LocalObservationDateTime'],
            "Температура (°C)": weather_data[0]['Temperature']['Metric']['Value'],
            "Ощущается как (°C)": weather_data[0]['RealFeelTemperature']['Metric']['Value'],
            "Влажность (%)": weather_data[0]['RelativeHumidity'],
            "Скорость ветра (км/ч)": weather_data[0]['Wind']['Speed']['Metric']['Value'],
            "Направление ветра": weather_data[0]['Wind']['Direction']['Localized'],
            "Видимость (км)": weather_data[0]['Visibility']['Metric']['Value'],
            "Давление (мбар)": weather_data[0]['Pressure']['Metric']['Value'],
            "Осадки (мм)": weather_data[0]['PrecipitationSummary']['Precipitation']['Metric']['Value']
        }

        return weather_information
    except requests.exceptions.RequestException as e:
        return {"error": f"Ошибка соединения с сервером: {str(e)}"}
    except ValueError as e:
        return {"error": str(e)}

def get_weather_by_coordinates(lat, lon):
    try:
        location_url = f'https://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={api_key}&q={lat},{lon}'
        location_response = requests.get(location_url, timeout=10)
        location_response.raise_for_status()

        location_data = location_response.json()
        if not location_data or 'Key' not in location_data:
            raise ValueError("Неверные координаты")

        location_key = location_data['Key']

        weather_url = f'https://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}&details=true'
        weather_response = requests.get(weather_url, timeout=10)
        weather_response.raise_for_status()

        weather_data = weather_response.json()
        if not weather_data:
            raise ValueError("Нет данных о погоде")

        weather_information = {
            "Время наблюдения": weather_data[0]['LocalObservationDateTime'],
            "Температура (°C)": weather_data[0]['Temperature']['Metric']['Value'],
            "Ощущается как (°C)": weather_data[0]['RealFeelTemperature']['Metric']['Value'],
            "Влажность (%)": weather_data[0]['RelativeHumidity'],
            "Скорость ветра (км/ч)": weather_data[0]['Wind']['Speed']['Metric']['Value'],
            "Направление ветра": weather_data[0]['Wind']['Direction']['Localized'],
            "Видимость (км)": weather_data[0]['Visibility']['Metric']['Value'],
            "Давление (мбар)": weather_data[0]['Pressure']['Metric']['Value'],
            "Осадки (мм)": weather_data[0]['PrecipitationSummary']['Precipitation']['Metric']['Value']
        }

        return weather_information
    except requests.exceptions.RequestException as e:
        return {"error": f"Ошибка соединения с сервером: {str(e)}"}
    except ValueError as e:
        return {"error": str(e)}

def check_bad_weather(weather_data):
    temperature = weather_data["Температура (°C)"]
    wind_speed = weather_data["Скорость ветра (км/ч)"]
    precipitation_probability = weather_data["Осадки (мм)"]
    humidity = weather_data["Влажность (%)"]
    pressure = weather_data["Давление (мбар)"]

    if temperature < 0 or temperature > 35: return "Неблагоприятные условия"
    if wind_speed > 50: return "Неблагоприятные условия"
    if precipitation_probability > 70: return "Неблагоприятные условия"
    if humidity and humidity > 85 and temperature > 30: return "Неблагоприятные условия"
    if pressure < 980 or pressure > 1030: return "Неблагоприятные условия"
    if wind_speed > 30 and temperature < 5: return "Неблагоприятные условия"
    if precipitation_probability > 50 and wind_speed > 30: return "Неблагоприятные условия"

    return "Благоприятные условия"