import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "83f854946ff60ace94550f462a45c936"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    weather_info = f"Weather in {city}:\n"
    weather_info += f"Temperature: {data['main']['temp']}°C\n"
    weather_info += f"Description: {data['weather'][0]['description']}"

    result_label.config(text=weather_info)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="", padx=10, pady=10)
result_label.pack()

root.mainloop()