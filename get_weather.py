import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    """Fetch weather data for a city and return it as a dictionary."""

    if not API_KEY:
        return {"error": "API key was not found in .env."}

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

        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
        }

    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            message = "The API key was rejected. Check or activate your key."
        elif response.status_code == 404:
            message = f"City '{city}' was not found."
        else:
            message = (
                f"Weather request failed with status code "
                f"{response.status_code}."
            )

        return {"error": message}

    except requests.exceptions.RequestException:
        return {
            "error": "Weather request failed. Check your internet connection."
        }


def print_weather(weather):
    """Print returned weather data in the terminal."""

    if "error" in weather:
        print(weather["error"])
        return

    print(f"\nWeather in {weather['city']}, {weather['country']}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Feels like: {weather['feels_like']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Description: {weather['description']}")


if __name__ == "__main__":
    city = input(
        "Enter a U.S. city, such as Durham,NC,US: "
    ).strip()

    if city:
        weather = get_weather(city)
        print_weather(weather)
    else:
        print("Please enter a city.")