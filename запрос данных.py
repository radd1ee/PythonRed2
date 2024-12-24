import requests
from API import api_key
url = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={api_key}&q=10%2C%2010'
print(requests.get(url).status_code)