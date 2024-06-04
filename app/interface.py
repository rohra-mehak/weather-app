from app.fetch_weather_data import WeatherFetcher
import asyncio
import os
import streamlit as st
from app.weather_bot import WeatherChatbot
import altair as alt

class WeatherApp:
    def __init__(self):
        self.data = None

    def handle_weather_query(self, city):
        if os.name == 'nt':
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        weather = WeatherFetcher(city_name=city)
        weather_data = asyncio.run(weather.get_weather())
        return weather_data

    def main_window(self):
        st.title("Hello! I'm Windy the weather bot")
        st.image(os.path.join(os.getcwd(), "app" ,"static", "weather-app-icon.jpg"), width=50)
        query = st.chat_input("Please enter your weather query")
        
        if query:
            bot = WeatherChatbot(query)
            response = bot.chatbot_response()
            print(response)
            if isinstance(response, tuple):
                city, processor_response = response
                st.write(processor_response)
                self.data =self.handle_weather_query(city=city)
                if self.data:
                    self.display_weather_data()
                    self.display_temperature_trend()
            else:
                st.warning(response)

    def display_weather_data(self):
        with st.expander("See details", expanded=True):
            st.write(f"Today is {self.data['description']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.header(self.data["temperature"])
                st.write("Temperature (C)")
                
            with col2:
                st.header(self.data["feels_like"])
                st.write("Feels Like (C)")
            col3, col4 = st.columns(2)
            with col3:
                st.header(self.data["visibility"])
                st.write("Visibility (km)")

            with col4:
                st.header(self.data["wind_speed"])
                st.write("Wind Speed (kmph)")

    def display_temperature_trend(self):
        with st.expander("See daily forecats", expanded=False):
                df = self.data["daily_forecasts"]
                chart = alt.Chart(df, title='Temperature Data').mark_bar(opacity=1).encode(
                column=alt.Column('Date:T', title="Date", spacing=60, header=alt.Header(labelOrient="bottom")),
                x=alt.X('Temperature Variant', sort=["Highest Temperature", "Lowest Temperature", "Current Temperature"], axis=None),
                y=alt.Y('value:Q', title='Temperature (C)'),
                color=alt.Color('Temperature Variant'),
                size = alt.value(30) 
            ).configure_view(stroke='transparent')

            # Display the chart
                st.altair_chart(chart)


if __name__ == "__main__":
    app = WeatherApp()
    app.main_window()



