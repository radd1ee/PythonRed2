import requests

url = "http://127.0.0.1:5000"

def test_home_page():
    response = requests.get(f"{url}/")
    print(f"Статус код главной страницы: {response.status_code}")
    print(f"Текст главной страницы:\n{response.text}")

def test_coordinates_form():
    response = requests.post(f"{url}/weather_choice", data={'choice': 'coordinates'})
    print(f"Статус код формы для координат: {response.status_code}")
    print(f"Текст формы для координат:\n{response.text}")

def test_cities_form():
    response = requests.post(f"{url}/weather_choice", data={'choice': 'cities'})
    print(f"Статус код формы для городов: {response.status_code}")
    print(f"Текст формы для городов:\n{response.text}")

def test_weather_by_valid_coordinates():
    data = {
        'lat1': '55.75',
        'lon1': '37.61',
        'lat2': '51.51',
        'lon2': '-0.13'
    }
    response = requests.post(f"{url}/weather_by_coordinates", data=data)
    print(f"Статус код запроса с координатами: {response.status_code}")
    print(f"Ответ на запрос с координатами:\n{response.text}")

def test_weather_by_invalid_coordinates():
    data = {
        'lat1': '999',
        'lon1': '999',
        'lat2': '999',
        'lon2': '999'
    }
    response = requests.post(f"{url}/weather_by_coordinates", data=data)
    print(f"Статус код запроса с невалидными координатами: {response.status_code}")
    print(f"Ответ на запрос с невалидными координатами:\n{response.text}")

def test_weather_by_valid_cities():
    data = {
        'city1': 'Moscow',
        'city2': 'London'
    }
    response = requests.post(f"{url}/weather_by_cities", data=data)
    print(f"Статус код запроса с городами: {response.status_code}")
    print(f"Ответ на запрос с городами:\n{response.text}")

def test_weather_by_invalid_cities():
    data = {
        'city1': 'FakeCity',
        'city2': 'AnotherFakeCity'
    }
    response = requests.post(f"{url}/weather_by_cities", data=data)
    print(f"Статус код запроса с невалидными городами: {response.status_code}")
    print(f"Ответ на запрос с невалидными городами:\n{response.text}")


test_home_page()
test_coordinates_form()
test_cities_form()
test_weather_by_valid_coordinates()
test_weather_by_invalid_coordinates()
test_weather_by_valid_cities()
test_weather_by_invalid_cities()
