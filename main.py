import requests
# Generated Api Key
api_key = "6311bdd8055d12e9d877464f3c124e12"

# url taken from openweather api with adding units=metric which return in celcious unit
url = "https://api.openweathermap.org/data/2.5/weather?units=metric&"

# Took the input from the user
city_name = input("Enter city name: ")

# Created final url with addition of api_key and city_name
Final_url = url + "appid=" + api_key + "&q=" + city_name

# added exception-handling
try:
    # store the json response in a variable
    response = requests.get(Final_url).json()

    # fetched temperature from json file
    temperature = response['main']['temp']
    min_temperature = response['main']['temp_min']
    max_temperature = response['main']['temp_max']

    # Printed the temperature
    print(f"The Temperature of {city_name} is {temperature}°C")
    print(f"Maximum_Temperature: {max_temperature}°C\nMinimum_Temperature: {min_temperature}°C")
except ValueError:
    print("Invalid city name")
except KeyError:
    print("Invalid Key")
