import python_weather
import asyncio
import os
import pandas as pd

class WeatherDataFetcher:
    def __init__(self, location='New York'):
        self.location = location
        self.weather_data = None

    async def fetch_weather(self):
        async with python_weather.Client() as client:
            self.weather_data = await client.get(location=self.location)

    def get_temperature(self):
        return self.weather_data.temperature if self.weather_data else None

    def get_description(self):
        return self.weather_data.description if self.weather_data else None

    def get_feels_like(self):
        return self.weather_data.feels_like if self.weather_data else None
    
    def get_wind_speed(self):
        return self.weather_data.wind_speed if self.weather_data else None
    
    def get_visibility(self):
        return self.weather_data.visibility if self.weather_data else None
        

    def get_daily_forecasts(self):
        if self.weather_data is not None:
            forecasts = {
                "Date": [],
                "Highest Temperature": [],
                "Lowest Temperature": [],
                "Temperature": []
            }

            for day in self.weather_data.daily_forecasts:
                forecasts["Date"].append(day.date)
                forecasts["Highest Temperature"].append(day.highest_temperature)
                forecasts["Lowest Temperature"].append(day.lowest_temperature)
                forecasts["Temperature"].append(day.temperature)

            df = pd.DataFrame(forecasts)
            temperature_df = df.melt(id_vars=["Date"], var_name="Temperature Variant", value_name="value")
            temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

            return temperature_df
        return None


    async def get_weather(self):
        await self.fetch_weather()
        return {
            "temperature": self.get_temperature(),
            "description": self.get_description(),
            "feels_like": self.get_feels_like(),
            "wind_speed": self.get_wind_speed(),
            "visibility": self.get_visibility(), 
            "daily_forecasts": self.get_daily_forecasts()
        }

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    location = input("enter city name")
    weather = WeatherDataFetcher(location)
    weather_data = asyncio.run(weather.get_weather())
    print(weather_data)
