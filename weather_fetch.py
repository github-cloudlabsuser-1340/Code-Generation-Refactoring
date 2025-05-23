import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"Weather in {city}: {weather['description'].capitalize()}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    api_key = "9e35862cde06aaa071d66a4a66751615"
    city = input("Enter city name: ")
    get_weather(city, api_key)