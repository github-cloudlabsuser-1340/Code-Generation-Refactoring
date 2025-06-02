# fetch weather data from openweathermap.org
import requests
def get_weather(city: str, api_key: str) -> dict:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch weather data", 
                "status_code": response.status_code,
                "message": response.text}


if __name__ == "__main__":
    city = "London"
    api_key = input("Enter your OpenWeatherMap API key: ")
    if not api_key:
        print("API key is required.")
        exit(1)
    weather_data = get_weather(city, api_key)
    print(weather_data)