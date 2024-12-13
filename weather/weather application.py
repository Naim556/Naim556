from tkinter import *
import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def search(event=None):
    search_city.get()
    error()

def error():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "01f674f7396d8a86ffa5553ee8563beb"
    CITY = search_city.get().capitalize()

    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url)

    if response.status_code == 404:
        label_not_write_city_name_and_error.config(text="I Can't Find The City.")
    elif search_city.get() == "":
        label_not_write_city_name_and_error.config(text="Please Enter The City Name.")
    else:
        label_not_write_city_name_and_error.config(text="")
        weather_answer(response.json())

def weather_answer(response):
    def kelvin_to_celsius_fahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = (9 / 5) * celsius + 32
        return celsius, fahrenheit

    temp_kelvin = response["main"]["temp"]
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response["main"]["feels_like"]
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed_get = response["wind"]["speed"]
    humidity_get = response["main"]["humidity"]
    description_get = response['weather'][0]['description']
    main_weather_description = response['weather'][0]['main']
    pressure_get = response["main"]["pressure"]

    coord_lon = response['coord']['lon']
    coord_lat = response['coord']['lat']
    time = TimezoneFinder()
    result = time.timezone_at(lng=coord_lon, lat=coord_lat)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")

    weather_show_the_answer(temp_celsius, feels_like_celsius, wind_speed_get, humidity_get, description_get,
                            pressure_get, current_time, main_weather_description, result)

def weather_show_the_answer(temp_celsius, feels_like_celsius, wind_speed_get, humidity_get, description_get,
                            pressure_get, current_time, main_weather_description, result):
    if main_weather_description == "Clouds":

        weather_label.config(image=image_cloudy_weather)

    elif main_weather_description == "Rain":

        weather_label.config(image=image_rainy_weather)

    elif main_weather_description == "Thunderstorm":

        weather_label.config(image=image_stormy_weather)

    elif main_weather_description == "Clear":

        weather_label.config(image=image_sunny_weather)

    elif main_weather_description == "Snow":

        weather_label.config(image=image_stormy_weather)

    else:
        pass

    label_city_information_temperature.config(text=f"{temp_celsius:.2f}°C")
    label_city_information_feel.config(text=f"Feels like Today: {feels_like_celsius:.2f}°C")
    label_city_information_weather_look.config(text=f"Weather Main: {main_weather_description}")
    label_timezone_cord.config(text=f"{result}")

    wind_speed_result.config(text=f"{wind_speed_get}m/s")
    humidity_result.config(text=f"{humidity_get}%")
    description_result.config(text=f"{description_get}")
    pressure_result.config(text=f"{pressure_get}")
    label_current_time1.config(text=f"{current_time}")


weather_application = Tk()

weather_application.title("Weather App")

weather_application.config(background="white")

weather_application.geometry("1000x500")

weather_application.resizable(width=False, height=False)

# weather Entry for search the city-------------------------------------------------------------------------------
search_city_var = StringVar()

search_back = PhotoImage(file="image//search back.png")
search_back_entry = Label(weather_application,
                          image=search_back,
                          background="white")
search_back_entry.place(relx=0.1, rely=0.1, anchor=NW)

search_city = Entry(search_back_entry,
                    background="#A7A9AC",
                    foreground="black",
                    font=(("Arial"), 20),
                    border=0,
                    textvariable=search_city_var)
search_city.place(relx=.05, rely=0, relwidth=.8, relheight=1, anchor=NW)
search_city.bind('<Return>', search)
# Button start the search
btn_image_search = PhotoImage(file="image//search_icon.png")
btn_search_city = Button(search_back_entry,
                         image=btn_image_search,
                         background="#A7A9AC",
                         border=0,
                         activebackground="#A7A9AC",
                         command=error)

btn_search_city.place(relx=.85, rely=0, relwidth=0.1, relheight=1, anchor=NW)

# this label show information for city------------------------------------------------------------------------------
#####################################################################################################################
image_rainy_weather = PhotoImage(file="image//rainy background.png")
image_sunny_weather = PhotoImage(file="image//sunny background.png")
image_snowy_weather = PhotoImage(file="image//snowy background.png")
image_cloudy_weather = PhotoImage(file="image//cloudy background.png")
image_stormy_weather = PhotoImage(file="image//stormy background.png")
image_all_weather = PhotoImage(file="image//weather a.png")

weather_label = Label(weather_application,
                      image=image_all_weather,
                      background="white")
weather_label.place(relx=0.35, rely=0.3, anchor=NW)

label_current_time = Label(weather_application,
                           text="Current City Time:",
                           font=("Arial", 23, "bold"),
                           background="white",
                           foreground="black")
label_current_time.place(relx=0.08, rely=0.27, anchor=NW)

label_current_time1 = Label(weather_application,
                            text="",
                            font=("Arial", 20, "bold"),
                            background="white",
                            foreground="black")
label_current_time1.place(relx=0.12, rely=0.37, anchor=NW)

label_city_information_temperature = Label(weather_application,
                                           text="",
                                           font=("Arial", 50, "bold"),
                                           background="white",
                                           foreground="red")
label_city_information_temperature.place(relx=0.56, rely=0.35, anchor=NW)

label_city_information_feel = Label(weather_application,
                                    text="",
                                    font=("Arial", 22, "bold"),
                                    background="white",
                                    foreground="black")
label_city_information_feel.place(relx=0.56, rely=0.50, anchor=NW)

label_city_information_weather_look = Label(weather_application,
                                            text="",
                                            font=("Arial", 22, "bold"),
                                            background="white",
                                            foreground="black")
label_city_information_weather_look.place(relx=0.56, rely=0.60, anchor=NW)

label_timezone_cord = Label(weather_application,
                            text="",
                            font=("Arial", 22, "bold"),
                            background="white",
                            foreground="black")
label_timezone_cord.place(relx=0.56, rely=0.27, anchor=NW)

#####################################################################################################################
#####################################################################################################################

information_label_image = PhotoImage(file="image//information back.png")

information_image_label = Label(weather_application,
                                image=information_label_image,
                                background="white")

information_image_label.place(relx=0.1, rely=0.75, anchor=NW)

wind_speed = Label(weather_application,
                   text=f"Wind Speed:",
                   font=("arial", 15, "bold"),
                   foreground="black",
                   background="#A7A9AC")
wind_speed.place(relx=0.15, rely=0.757, relwidth=0.15, relheight=0.07, anchor=NW)

wind_speed_result = Label(weather_application,
                          text=f"...",
                          font=("arial", 15, "bold"),
                          foreground="black",
                          background="#A7A9AC")
wind_speed_result.place(relx=0.15, rely=0.827, relwidth=0.15, relheight=0.12, anchor=NW)

humidity = Label(weather_application,
                 text=f"Humidity:",
                 font=("arial", 15, "bold"),
                 foreground="black",
                 background="#A7A9AC")
humidity.place(relx=0.33, rely=0.757, relwidth=0.15, relheight=0.07, anchor=NW)

humidity_result = Label(weather_application,
                        text=f"...",
                        font=("arial", 15, "bold"),
                        foreground="black",
                        background="#A7A9AC")
humidity_result.place(relx=0.33, rely=0.827, relwidth=0.15, relheight=0.12, anchor=NW)

description = Label(weather_application,
                    text=f"Description:",
                    font=("arial", 15, "bold"),
                    foreground="black",
                    background="#A7A9AC")
description.place(relx=0.52, rely=0.757, relwidth=0.15, relheight=0.07, anchor=NW)

description_result = Label(weather_application,
                           text=f"...",
                           font=("arial", 15, "bold"),
                           foreground="black",
                           background="#A7A9AC")
description_result.place(relx=0.50, rely=0.827, relwidth=0.2, relheight=0.12, anchor=NW)

pressure = Label(weather_application,
                 text=f"Pressure:",
                 font=("arial", 15, "bold"),
                 foreground="black",
                 background="#A7A9AC")
pressure.place(relx=0.7, rely=0.757, relwidth=0.15, relheight=0.07, anchor=NW)

pressure_result = Label(weather_application,
                        text=f"...",
                        font=("arial", 15, "bold"),
                        foreground="black",
                        background="#A7A9AC")
pressure_result.place(relx=0.7, rely=0.827, relwidth=0.15, relheight=0.12, anchor=NW)

#######################################################################################################################
#######################################################################################################################
## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ## ERROR ##

label_not_write_city_name_and_error = Label(weather_application,
                                            text="",
                                            background="white",
                                            foreground="red",
                                            font=("Arial", 15))
label_not_write_city_name_and_error.place(relx=0.15, rely=0.22, anchor=NW)

#######################################################################################################################
#######################################################################################################################
weather_application.mainloop()
