# Weather Report CLI

A command-line Python application that retrieves current weather information for a U.S. city using the OpenWeather API.

## Features

- Accepts a city through terminal input
- Displays the current temperature in Celsius
- Displays the “feels like” temperature
- Displays humidity
- Displays a weather description
- Handles missing cities, invalid API keys, and connection errors

## Requirements

- Python 3
- An OpenWeather API key

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

3. Create a file named `.env` in the project folder:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Do not share or commit your `.env` file.

## Run the Application

```bash
python3 get_weather.py
```

When prompted, enter a city using this format:

```text
Durham,NC,US
```

## Example Output

```text
Weather in Durham,NC,US:
Temperature: 26.35°C
Feels like: 26.35°C
Humidity: 56%
Description: Overcast Clouds
```
