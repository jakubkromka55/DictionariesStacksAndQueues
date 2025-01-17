import json

# Otwórz plik JSON w trybie odczytu z kodowaniem UTF-8
with open('dogs.json', 'r', encoding='utf-8') as file:
    # Załaduj dane z pliku JSON do zmiennej
    data = json.load(file)

# Iterujemy przez listę psów
for dog in data:
    # Sprawdzamy, czy wiek psa jest mniejszy niż 5
    if dog['age'] < 5:
        # Drukujemy informacje o psie
        print(f"Name: {dog['name']}")
        print(f"Breed: {dog['breed']}")
        print(f"Age: {dog['age']}")
        print(f"Weight: {dog['weight_kg']} kg")
        print(f"Owner: {dog['owner']}")
        print(f"Vaccinated: {'Yes' if dog['vaccinated'] else 'No'}")
        print()  # Pusta linia oddzielająca dane o psach
