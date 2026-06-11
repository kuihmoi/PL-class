# import requests
# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)

# if response.status_code == 200:
#     post = response.json()
#     print("First post title:", post[0]['title'])
# else:
#     print("Failed to retrieve posts. Status code:", response.status_code)

# query paramters - adding parameters to the url
import requests

api_key = "5be5bc3bd1299fca70a7f3692341faa3"

city = "Seoul"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Description: {data['weather'][0]['description']}")
else:
    print(f"Error:", response.status_code, response.text)
    print("Could not retrieve weather data.")

import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    print("post created", response.json())
else:
    print("Failed:", response.status_code, response.text)