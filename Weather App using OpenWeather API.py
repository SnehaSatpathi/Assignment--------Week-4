import requests

API_KEY = "your_api_key_here"
city = "Durgapur"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(f"Weather in {city}: {data['weather'][0]['description']}")
print(f"Temperature: {data['main']['temp']}°C")
