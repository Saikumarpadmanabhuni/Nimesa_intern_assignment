import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_weather_by_date(data, date):
    for entry in data['list']:
        if entry['dt_txt'].startswith(date):
            return entry['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for entry in data['list']:
        if entry['dt_txt'].startswith(date):
            return entry['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for entry in data['list']:
        if entry['dt_txt'].startswith(date):
            return entry['main']['pressure']
    return None

def main():
    data = get_weather_data()
    if not data:
        return

    while True:
        print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            temperature = get_weather_by_date(data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("No data found for the given date.")
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("No data found for the given date.")
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No data found for the given date.")
        else:
            print("Invalid choice. Please select a valid option.")


main()