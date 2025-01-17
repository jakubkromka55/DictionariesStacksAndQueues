import json

# Otwórz plik JSON w trybie odczytu z kodowaniem UTF-8
with open('cities.json', 'r', encoding='utf-8') as file:
    # Załaduj dane z pliku JSON do zmiennej
    data = json.load(file)

# Przechodzimy przez każde miasto w tablicy
for city in data:
    # Iterujemy po kluczach i wartościach w słowniku każdego miasta
    for key, value in city.items():
        print(f"{key}: {value}")
    print()  # Dodajemy pustą linię po każdym mieście
