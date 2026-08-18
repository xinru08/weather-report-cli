import os

import requests
from dotenv import load_dotenv


# Load variables from the .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    """Fetch and display the current weather for a city."""

    if not API_KEY:
        print("API key was not found in .env.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.title()}")

    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            print("The API key was rejected. Check or activate your key.")
        elif response.status_code == 404:
            print(f"City '{city}' was not found.")
        else:
            print(f"Weather request failed with status code {response.status_code}.")

    except requests.exceptions.RequestException:
        print("Weather request failed. Check your internet connection.")


if __name__ == "__main__":
    city = input("Enter a U.S. city, such as Durham,NC,US: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a city.")