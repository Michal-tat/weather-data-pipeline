import requests
import json
import os

# To jest nasz link do API (Kraków, dane od 2020 do 2023 roku)
API_URL = "https://archive-api.open-meteo.com/v1/archive?latitude=50.0614&longitude=19.9366&start_date=2020-01-01&end_date=2023-12-31&hourly=temperature_2m,precipitation&timezone=Europe%2FWarsaw"

def fetch_weather_data():
    print("🚀 Łączę się z bazą Open-Meteo...")
    
    # Uderzamy do API
    response = requests.get(API_URL)
    
    # Sprawdzamy, czy serwer nie zwrócił błędu (np. 404 albo 500)
    response.raise_for_status()
    
    # Zamieniamy odpowiedź na format JSON (słownik w Pythonie)
    data = response.json()
    print("✅ Dane pobrane pomyślnie!")
    
    return data

def save_data(data):
    # Tworzymy folder 'data', jeśli go jeszcze nie ma
    if not os.path.exists('data'):
        os.makedirs('data')
        
    filepath = os.path.join('data', 'pogoda_krakow_surowa.json')
    
    # Zapisujemy nasz słownik do pliku .json z ładnym wcięciem (indent=4), żeby dało się to czytać
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"💾 Zapisano plik twardo na dysku: {filepath}")

if __name__ == "__main__":
    # Uruchamiamy nasz proces
    dane_pogodowe = fetch_weather_data()
    save_data(dane_pogodowe)