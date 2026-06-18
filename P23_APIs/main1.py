import pandas as pd
import os
import requests

"""
1) WEATHER API WITH API KEY
Use an API that requires authentication
OpenWeatherMap
The key identifies that user or application.
Set and environemnt variable"
                OPENWEATHER_API_KEY=...
                https://openweathermap.org/city/2643743
                Sign up/ sign in/ user name/ My Api Keys/generate key
"""
api_key = "ed102db6853f408b92c23bce7a5574d8"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Seoul",
    "appid": api_key,
    "units": "metric"
}
try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Weather: {data['weather'][0]['description']}")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    print(response.txt)
except requests.exceptions.RequestException as e:
    print("Request Error", e)

"""
Most modern APIs work over the Internet using HTTP
the others are WebSocket, gRPC, GraphQL, SOAP, etc.

Common HTTP methods:
    GET     : read data
    POST    : create data
    PUT     : update or replace data
    PATCH   : partially update data
    DELETE  : delete data

Common HTTP status codes:
    200 : Success
    201 : Created
    400 : Bad Request
    401 : Unauthorized
    403 : Forbidden
    404 : Not Found
    429 : Too Many Requests
    500 : Server Error

Most APIs return data in JSON format.

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
country = "South Korea"
url = f"https://rescountries.com/v3.1/name/{country}"
params = {
    "fields": "name, capital, region, population, languages, currencies, flags"
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    first_match = data[0]
    name = first_match["name"]["common"]
    capital = first_match["capital"][0]
    region = first_match["region"]
    population = first_match["population"]
    languages = first_match["languages", {}]
    currencies = first_match.get("currencies", {})
    print("Country:", name)
    print("Capital:", capital)
    print("Region:", region)
    print("Population:", population)
    print("Languages:", list(languages.values()))
else:
    print("Error:", response.status_code)
    print(response.text)

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
print("Capital:", capital)
print("Population:", population)
print("Latitude:", latitude)
print("Longitude:", longitude)
print("Temperature:", current["temperature_2m"], "°C")
print("Humidity:", current["relative_humidity_2m"], "%")
print("Country:", current["wind_speed_10m"], "km/h")

# ---------------------------------------------------------------------------------

"""
7) download image or file
API responses are not always JSON
Some APIs return binary data such as images or files.
We use response.content instead or response.json()
"""
image_url = "https://www.google.com/imgres?q=cat&imgurl=https%3A%2F%2Fwww.cats.org.uk%2Fmedia%2F13139%2F220325case013.jpg&imgrefurl=https%3A%2F%2Fwww.cats.org.uk%2Fcats-blog%2F9-things-to-know-before-getting-your-first-cat&docid=BJaHVuqp-vSSnM&tbnid=KJJtoL7e6aITTM&vet=12ahUKEwiZx5HV54-VAxVtd_UHHW6uK9cQnPAOegQIFBAB..i&w=8192&h=5464&hcb=2&ved=2ahUKEwiZx5HV54-VAxVtd_UHHW6uK9cQnPAOegQIFBAB"
response = requests.get(image_url, timeout=10)
if response.status_code == 200:
    filename = "downloaded_image.jpg"
    with open(filename, "wb") as file:
        file.write(response.content)
    print("Image downloaded as: ", filename)
else:
    print("Error: ", response.status_code)

# -----8) download a dataset
url = "https://github.com/datasciencedojo/datasets/blob/f0ccab6a7ceafdff780052166fb6fab3311398eb/titanic.csv"
response = requests.get(url)
if response.status_code == 200:
    with open("titanic.csv", "wb") as file:
        file.write(response.content)
    print("Dataset downloaded successfully.")
else:
    print("Error:", response.status_code)

# ----- 9) download house price dataset
url = (
    "https://raw.githubusercontent.com"
    "ageron/handson-ml/master/dataset/housing/housing.csv"
)
filename = "housing.csv"
response = requests.get(url)
if response.status_code == 200:
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Dataset saved as '{filename}'")
    housing = pd.read_csv(filename)
    print("\nFirst 5 rows:")
    print(housing.head()) 
    print("\nShape:", housing.shape)
else:
    print("Error:", response.status_code)

# ---------------------------------------------------------------------------------

"""
10) bitcoin price api
"""
# url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()
#     data = response.json()
#     print("Bitcoin Price (USD):")
#     print(data["data"]["amount"])
# except

# ---------------------------------------------------------------------------------
# 13) Exchange rate API
url = "https://open.er-api.com/v6/latest/USD"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("USD to KRW:")
    print(data["rates"]["KRW"])
    print("USD to EUR:")
    print(data["rates"]["EUR"])
else:
    print("Error:", response.status_code)

# ---------------------------------------------------------------------------------
# 14) flight into API
# https://aviationstack.com/dashboard
# api_key = "..."
# url = "http://api.aviationstack.com/v1/flights"
# params = {
#     "access_key": api_key,
#     "flight_iata": "KE012"
# }
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     data = response.json()
#     if data["data"]:
#         flight = data["data"][0]
#         print("Airline",
#               flight["airline"]["name"])
#         print("Status:",
#               flight["flight status"])