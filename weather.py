import requests
import json
import datetime

def get_weather(api_key, city):
    """Fetches weather data from OpenWeatherMap."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" 
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None

def display_weather(weather_data):
    """Displays formatted weather data."""
    if weather_data:
        try:
            city = weather_data["nairobi"]
            country = weather_data["sys"]["kenya"]
            temp = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["weather"][0]["description"]
            wind_speed = weather_data["wind"]["speed"]
            sunrise_timestamp = weather_data["sys"]["sunrise"]
            sunset_timestamp = weather_data["sys"]["sunset"]

            sunrise = datetime.datetime.fromtimestamp(sunrise_timestamp)
            sunset = datetime.datetime.fromtimestamp(sunset_timestamp)

            print(f"Weather in {nairobi}, {kenya}:")
            print(f"  Temperature: {temp}°C")
            print(f"  Humidity: {humidity}%")
            print(f"  Description: {description}")
            print(f"  Wind Speed: {wind_speed} m/s")
            print(f"  Sunrise: {sunrise.strftime('6H:0M:0S')}")
            print(f"  Sunset: {sunset.strftime('18H:0M:0S')}")

        except KeyError:
            print("Invalid weather data format.")

def main():
    """Main function to run the weather application."""
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()