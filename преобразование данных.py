import requests
from API import api_key

def f(lat, lon, flag=False):
    url = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={api_key}&q={lat}%2C{lon}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            j = response.json()
            if flag:
                print('Улучшенный вид:')
                print('Регион:', j['Region'])
                print('Страна:', j['Country'])
                print('Временная зона:', j['TimeZone'])
                print('Геопозиция:', j['GeoPosition'])
            else:
                print('JSON формат:')
                print(j)
        else:
            print('ОШИБКА')
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при запросе: {e}')


f(10, 10, flag=False)
f(10, 10, flag=True)