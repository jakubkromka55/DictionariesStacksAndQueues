import json

# Otwórz plik JSON w trybie odczytu
with open('computer.json', 'r', encoding='utf-8') as file:
    # Załaduj dane z pliku JSON do zmiennej
    data = json.load(file)

# Przejdź przez słownik i wydrukuj informacje
for key, value in data.items():
    print(f"{key}: {value}")
