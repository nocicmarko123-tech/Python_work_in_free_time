import requests
from geopy.geocoders import Nominatim

place = input("Enter the city name: ").strip()
country = input("Enter the country name: ").strip()
where = f"{place}, {country}"

geolocator = Nominatim(user_agent="weather_project_app")
location = geolocator.geocode(where)
latitude = location.latitude
longitude = location.longitude

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
response = requests.get(url).json()

print(f"{where.title()}: {response['current']['temperature_2m']}°C")
