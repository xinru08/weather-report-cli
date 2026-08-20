# Weather Report App

A Python weather application that retrieves current weather data from the OpenWeather API. It can run as either a command-line program or an interactive Streamlit web app.

## Live App

Try the deployed application:

https://weather-report-cli-js7nf8utn9gw3xabbd9rbs.streamlit.app

## Python Version

Developed and tested with Python 3.10.0.

## Features

- Accepts a U.S. city from user input
- Calls the OpenWeather API
- Displays temperature in Celsius
- Displays the “feels like” temperature
- Displays humidity and weather conditions
- Provides both CLI and Streamlit interfaces
- Handles invalid cities, missing API keys, and connection errors

## Project Files

- `get_weather.py` — retrieves weather data and provides the CLI
- `streamlit_app.py` — provides the Streamlit web interface
- `requirements.txt` — lists required Python packages
- `.env` — stores the private OpenWeather API key and is not committed

## Setup

1. Clone the repository:

```bash
git clone https://github.com/xinru08/weather-report-cli.git
cd weather-report-cli
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

4. Create a `.env` file in the project directory:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Do not share or commit the `.env` file.

## Run the Streamlit App

```bash
python3 -m streamlit run streamlit_app.py
```

The application should open in your browser at:

```text
http://localhost:8501
```

Enter a city using a format such as:

```text
Durham,NC,US
```

To stop the Streamlit server, press `Control+C` in the terminal.

## Run the Command-Line Version

```bash
python3 get_weather.py
```
