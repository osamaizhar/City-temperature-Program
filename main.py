import requests

def get_temperature(city_name):
    # Geocoding to get the latitude and longitude of the city
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    geo_response = requests.get(geocoding_url)

    if geo_response.status_code == 200:
        geo_data = geo_response.json()
        if geo_data['results']:
            # Get latitude and longitude of the city
            latitude = geo_data['results'][0]['latitude']
            longitude = geo_data['results'][0]['longitude']
            
            # Fetch weather data using the coordinates
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
            weather_response = requests.get(weather_url)
            
            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                temperature_celsius = weather_data['current_weather']['temperature']
                temperature_fahrenheit = (temperature_celsius * 9/5) + 32
                return temperature_celsius, temperature_fahrenheit
    return None

# Example city name
city = input("Enter the city name: ")

# Get the temperature
celsius, fahrenheit = get_temperature(city)

if celsius and fahrenheit:
    print(f"Temperature in {city}: {celsius:.2f}°C / {fahrenheit:.2f}°F")
else:
    print("Couldn't retrieve temperature data.")
