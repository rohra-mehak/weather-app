# Weather App

## Description
The Weather App is a simple chatbot that provides real-time weather information and trends based on weather related user queries. It utilizes Python-Weather, Streamlit, and spaCy to fetch weather data and process user input.

## Pre-Requsites
1. Python 3.x
2. pip (tool for installing and using Python packages)

## How to Run
1. Clone the repository:

   git clone https://github.com/rohra-mehak/weather-app.git

2. Navigate to the project directory:

   cd weather-app

3. Install dependencies:

   pip install -r requirements.txt

   Alternatively you can install them manually using pip. 

4. run the app:

   streamlit run main.py

## Usage
### Input: 
Enter your weather-related queries in the provided text box of the interface. You can ask about the weather conditions in specific cities or locations.
You can try queries such as:

     a. What is the current weather in Wroclaw ?
     b. Is it sunny in London ?
     c. How is the weather in New Delhi ?
     d. Current temperature in New York

### Output: 
The chatbot will process your query , determine a location and display the relevant weather information for that location including temperature,wind speed, and weather condition.
Fore more information on forecasts and variantions in trends, detailed information more tabs can be viewed.

## Features
1. Processes general weather related user queries with a location
2. Fetch current weather data for any location.
3. Displays current weather information for a location
4. Displays hourly temperature trends
5. Displays a high/low temperature forecasts for coming days.
6. Displays additional hourly information such wind speed, humidity, temperature forecasts.

## Sample Snapshots

### Initial Screen

![Initial Screen](https://github.com/rohra-mehak/weather-app/blob/main/app/static/snapshot_weather_app_initial.png?raw=true)

### Input Query
![Input Query](https://github.com/rohra-mehak/weather-app/blob/main/app/static/snapshot_weather_app_input_query.png?raw=true)

### Current Weather Information Display
![Current Weather Information Display](https://github.com/rohra-mehak/weather-app/blob/main/app/static/snapshot_weather_app_weather_info.png?raw=true)

### View Hourly Temperature Trend
![View Hourly Temperature Trend](https://github.com/rohra-mehak/weather-app/blob/main/app/static/snapshot_weather_app_hourly_temperature_trend.png?raw=true)

### View Temeprature Spike
![View Temeprature Spike](https://github.com/rohra-mehak/weather-app/blob/main/app/static/snapshot_weather_app_high_low_temp.png?raw=true)





