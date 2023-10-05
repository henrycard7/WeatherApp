import tkinter as tk
import requests
from PIL import Image, ImageTk  # Pillow library for handling images

background_color = "#739fe6"
button_color = "#32353d"
text_color = "#370d6e"
text_box_color = "#b4bef0"

# Absolute file path to the icons directory
icons_directory = r'C:\Users\henry\PycharmProjects\weather\icons'


# Weather condition to icon mapping
weather_icons = {
    "Clear": f"{icons_directory}\\sun.png",
    "Clouds": f"{icons_directory}\\cloud.png",
    "Rain": f"{icons_directory}\\rain.png",

    # Add more weather conditions and their corresponding icons as needed
}


def get_weather():
    city = city_entry.get()
    api_key = "83f854946ff60ace94550f462a45c936"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # weather_info = f"Weather in {city}:\n"
    # weather_info += f"Temperature: {data['main']['temp'] - 273.15}°C\n"
    # #temperature_celsius = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    # weather_info += f"Description: {data['weather'][0]['description']}"
    #
    # result_label.config(text=weather_info)
    if response.status_code == 200:
        temperature_celsius = data['main']['temp'] - 273.15
        weather_description = data['weather'][0]['description']
        weather_info = f"Weather in {city}:\n"
        weather_info += f"Temperature: {temperature_celsius:.2f}°C\n"
        weather_info += f"Description: {weather_description}"
        # Display weather icon based on weather condition
        weather_condition = data['weather'][0]['main']
        if weather_condition in weather_icons:
            icon_path = weather_icons[weather_condition]
            weather_icon = Image.open(icon_path)
            weather_icon = ImageTk.PhotoImage(weather_icon)
            icon_label.config(image=weather_icon)
            icon_label.image = weather_icon  # Keep a reference to avoid garbage collection

        result_label.config(text=weather_info, fg=text_color)
    else:
        result_label.config(text="Error: Unable to fetch weather data")


# Create the main window
root = tk.Tk()
root.title("Weather App")
# Apply custom colors
root.configure(bg=background_color)

# Create and place widgets
city_label = tk.Label(root, text="Enter City:", bg=background_color, fg=text_color)
city_label.pack()

city_entry = tk.Entry(root, bg=text_box_color)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, bg=button_color, fg="white")
get_weather_button.pack()

# Create an empty label for displaying the weather icon
icon_label = tk.Label(root, bg=background_color)
icon_label.pack()

result_label = tk.Label(root, text="", padx=10, pady=10, bg=background_color, fg=text_color)
result_label.pack()

root.mainloop()
