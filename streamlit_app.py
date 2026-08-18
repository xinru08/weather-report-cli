import streamlit as st

from get_weather import get_weather


def choose_weather_emoji(description):
    """Choose an emoji based on the weather description."""

    description = description.lower()

    if "clear" in description:
        return "☀️"
    if "cloud" in description:
        return "☁️"
    if "rain" in description:
        return "🌧️"
    if "snow" in description:
        return "❄️"
    if "storm" in description or "thunder" in description:
        return "⛈️"

    return "🌤️"


st.set_page_config(
    page_title="Weather Report",
    page_icon="🌤️",
)

st.title("🌤️ Weather Report")
st.write("Enter a U.S. city to view its current weather.")

city = st.text_input(
    "City",
    placeholder="For example: Durham,NC,US",
)

if st.button("Get Weather", type="primary"):
    if not city.strip():
        st.warning("Please enter a city.")
    else:
        with st.spinner("Checking the weather..."):
            weather = get_weather(city.strip())

        if "error" in weather:
            st.error(weather["error"])
        else:
            emoji = choose_weather_emoji(weather["description"])

            st.subheader(
                f"{emoji} Weather in "
                f"{weather['city']}, {weather['country']}"
            )

            temperature_column, feels_column, humidity_column = st.columns(3)

            temperature_column.metric(
                "Temperature",
                f"{weather['temperature']}°C",
            )

            feels_column.metric(
                "Feels Like",
                f"{weather['feels_like']}°C",
            )

            humidity_column.metric(
                "Humidity",
                f"{weather['humidity']}%",
            )

            st.info(f"Conditions: {weather['description']}")