import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            city_name = data['name']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_description = data['weather'][0]['description']
            
            weather_message = (
                f"Weather in {city_name}:\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {weather_description.capitalize()}"
            )
            
            messagebox.showinfo("Weather Information", weather_message)
        else:
            
            messagebox.showerror("Error", f"Could not retrieve weather data. Status code: {response.status_code}")
    except Exception as e:
        
        messagebox.showerror("Error", f"Error: {e}")


def on_search_button_click():
    city = city_entry.get()
    if city:
        get_weather(city, api_key)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

root = tk.Tk()
root.title("Weather App")

api_key = "6b22ae01f3486aa64678d8703ebb939b"

label = tk.Label(root, text="Enter City Name:", font=("Arial", 14))
label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=on_search_button_click)
search_button.pack(pady=20)

root.mainloop()
