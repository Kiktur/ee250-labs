"""Fetches and displays current weather conditions for a given city using the WeatherAPI."""
import requests

# WeatherAPI key
# https://official-joke-api.appspot.com/random_joke
WEATHER_API_KEY = ''  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    """Fetches and displays current weather conditions for a given city.
    
    Args: 
        city: Name of the city in string accepted by the weatherAPI
    
    Raises: 
        requests.RequestException: If the API request is unsuccessful.
        KeyError: If expected fields are missing in the API response.
    """
    # Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    # Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(url)
    # Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    #print(f"GET Status Code: {response.status_code}")
    #print(f"GET Response Body: {response.text}")
    data = response.json()
    
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # Parse the JSON data returned by the API. Extract and process the following information:
        print(f"Weather data for {city}:")
        # - Current temperature in Fahrenheit
        print(f"Temp: {data['current']['temp_f']}")
        # - The "feels like" temperature
        print(f"Feels like: {data['current']['feelslike_f']}")
        # - Weather condition (e.g., sunny, cloudy, rainy)
        print(f"Weather condition: {data['current']['condition']['text']}")
        # - Humidity percentage
        print(f"Humidity: {data['current']['humidity']}")
        # - Wind speed and direction
        print(f"Wind speed (mph): {data['current']['wind_mph']}")
        # - Atmospheric pressure in mb
        # - UV Index value
        print(f"UV: {data['current']['uv']}")
        # - Cloud cover percentage
        print(f"Cloud cover %: {data['current']['cloud']}")
        # - Visibility in miles
        print(f"Vis Miles: {data['current']['vis_miles']}")
    
    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    #Prompt the user to input a city name.
    city = input("Input city: ")
    get_weather(city)
    #Call the 'get_weather' function with the city name provided by the user.
    pass
