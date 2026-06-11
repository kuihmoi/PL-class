import pandas as pd
import os
import requests

"""
1) WEATHER API WITH API KEY
Use

- buat kat rumah ada gambar
"""



# ---------------------------------------------------------------------------------
"""
2) GITHUB USER PROFILE API
API: Github REST API
Public Github profile data can be fetched without authentication
"""

username = ""
url = f"https://api.github.com/users/{username}"
headers = {
    "Accept": "application/vnd.github+json"
}
token = os.gatenv("GITHUB_TOKEN")
if token:
    headers["Authorization"] = f"Bearer {token}"
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print("Username:", data["login"])
    print("Name:", data["name"])
    print("Public repositories:", data["public"])
    print("Followers:", data["followers"])
    print("Profile URL:", data["html_url"])
else:
    print("Error:", response.status_code)
    print(response.text)
    
# ---------------------------------------------------------------------------------
"""
3) rest countries api
Use an API that returns rich nested JSON.
API: REST Countries v3.1
Many APIs return nested dictionaries and lists.
"""
# country = "South Korea"
# url = f"https://rescountries.com/v3.1/name/{country}"
# params = {
#     "fields": "name, capital, region, population, languages, currencies, flags"
# }
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     data = response.json()
#     first_match = data[0]
#     name = first_match["name"]["common"]
#     capital = first_match["capital"][0]
#     region = first_match["region"]
#     population = first_match["population"]
#     languages = first_match["languages", {}]
#     currencies = first_match.get("currencies", {})
#     print("Country:", name)
#     print("Capital:", capital)
#     print("Region:", region)
#     print("Population:", population)
#     print("Languages:", list(languages.values()))
# else:
#     #tak habis

# ---------------------------------------------------------------------------------
"""
4) NASA astronomy picture of the day
API: NASA APOD API
Some APIs provide a demo key
- need to generate a key to get information
"""

api_key = "DEMO_KEY"
url = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": api_key
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print("Title:", data.get("title"))
    print("Date:", data.get("date"))
    print("Media Type:", data.get("media_type"))
    print("URL:", data.get("url"))
    print("\nExplanation:")
    print(data.get("explanation", "")[:500], "...")
else:
    print("Error:", response.status_code)
    print(response.text)

# ---------------------------------------------------------------------------------
"""
5) open-meteo api without api key
Use a weather API without an API key
API: Open-Meteo
hourly temparature for Seoul
"""

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 37.5665,
    "longitude": 126.9780,
    "hourly": "temparatur_2m",
    "forecast_days": 1,
    "timezone": "Asia/Seoul"
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    times = data["hourly"]["time"]
    temparatures = data["hourly"]["temparature_2m"]
    print("First 5 hourly forecasts for Seoul:")
    for t, temp in zip(times[:5], temparatures[:5]):
        print(t, ":", temp, "C") #degree c unit
else:
    print("Error:", response.status_code)
    print(response.text)

# ---------------------------------------------------------------------------------
"""
6) Two APIs
Combine multiple APIs in oen small project
APIs:1. Rest Countries API
     2. Open-Meteo API
Workflow:
        1. Get country information
        2. Extract capital city and coordinates
        3. Use coordinates to fetch weather forecast.
"""
country = "Japan"
country_url = f"https://restcountries.com/v3.1/name/{country}"
country_params = {
    "fields": "name, capital, capitalInfo, population, region"
}
country_response = requests.get(country_url, params=params)
if country_response.status_code != 200:
    print("Could not fetch country data.")
    print(country_response.status_code, country_response.text)
country_data = country_response.json()[0]
country_name = country_data["name"]["common"]
capital = country_data["population"]
region = country_data["region"]
latlng = country_data["capitalInfo"]["latlng"]
latitude = latlng[0]
longitude = latlng[1]
weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m, relative_humidity_2m, wind_speed_10m",
    "timezone": "auto"
}
weather_response = requests.get(weather_url, params=weather_params)
if weather_response.status_code != 200:
    print("Could not fetch country data.")
    print(weather_response.status_code, weather_response.text)
weather_data = weather_response.json()
current = weather_data["current"]
print("Country:", country_name)
print("Region:", region)
print("Country:", country_name)
print("Country:", country_name)
print("Country:", country_name)
print("Country:", country_name)
print("Country:", country_name)
print("Country:", country_name)
print("Country:", country_name)
