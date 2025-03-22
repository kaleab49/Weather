import requests
import customtkinter as ctk

API_KEY = open("api.txt").read().strip()  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
units = "metric"


def get_weather():
    city = city_entry.get()
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units={units}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data["main"]["temp"]

        # Update the labels with weather information
        weather_label.configure(text=f"Weather: {weather}")
        temp_label.configure(text=f"Temperature: {temperature}")
    else:
        weather_label.configure(text="An error occurred.")
        temp_label.configure(text="")

root = ctk.CTk()
root.title("Weather App")
root.geometry("400x300")


city_label = ctk.CTkLabel(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = ctk.CTkEntry(root, width=200)
city_entry.pack(pady=10)

get_weather_button = ctk.CTkButton(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

weather_label = ctk.CTkLabel(root, text="Weather: ", font=("Arial", 14))
weather_label.pack(pady=5)

temp_label = ctk.CTkLabel(root, text="Temperature: ", font=("Arial", 14))
temp_label.pack(pady=5)

# Run the application
root.mainloop()
