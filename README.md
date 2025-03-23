# Weather App

This is a simple Weather App built using Python with the `customtkinter` module for the GUI and the `requests` module to fetch weather data from the OpenWeatherMap API.

## Features
- Fetches current weather and temperature for a specified city.
- Displays weather conditions and temperature in a user-friendly interface.
- Uses the OpenWeatherMap API to retrieve weather data.

## Requirements
Make sure you have the following installed:
- Python 3.x
- `requests` module
- `customtkinter` module

## Installation
1. Clone or download this repository.
2. Install required dependencies:
   ```bash
   pip install requests customtkinter
   ```
3. Create a file named `api.txt` in the same directory and paste your OpenWeatherMap API key inside it.

## Usage
1. Run the script:
   ```bash
   python weather_app.py
   ```
2. Enter the name of the city in the input field.
3. Click the "Get Weather" button to fetch and display weather details.

## API Key Setup
- Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
- Save the key inside a file named `api.txt` in the same directory as the script.

## License
This project is open-source and available under the MIT License.

