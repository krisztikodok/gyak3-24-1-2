"""
import requests
import json

#weather application
print("***WEATHER***")
mycity=input("Please enter the city:")
api_key="9fiaz0uanaa7gmhmtrlg4zfbr2hqi7wh"
url=f"http://api.openweathermap.org/data/2.5/weather?q=+{mycity}&appid={api_key}"
response=requests.get(url)
if __name__=="__main__":
  data=response.json()
  main=data['main']
  temp=main['temp']
  hum=main['humidity']
  pres=main['pressure']
  wea=data['weather']
  wind=main['wind']
  print(f"Weather in {mycity}:")
  print(f"Temperature: {temp} Kelvin")
  print(f"Humidity: {hum}")

import requests, json

api_key = "Your_API_Key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    wind_speed = x["wind"]["speed"]
    snow = x.get("snow", {}).get("3h", 0)  # Snow volume for the last 3 hours
    rain = x.get("rain", {}).get("3h", 0)  # Rain volume for the last 3 hours

    print(f"Temperature (in kelvin unit) = {current_temperature}")
    print(f"Atmospheric pressure (in hPa unit) = {current_pressure}")
    print(f"Humidity (in percentage) = {current_humidity}")
    print(f"Description = {weather_description}")
    print(f"Wind Speed = {wind_speed}")
    print(f"Snow Volume (last 3 hours) = {snow}")
    print(f"Rain Volume (last 3 hours) = {rain}")
else:
    print("City Not Found")
"""
