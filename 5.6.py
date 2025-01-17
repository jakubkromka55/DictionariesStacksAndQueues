# Program tworzy słownik 'person' zawierający dane z dwóch innych słowników

# Podstawowe dane osobowe
basic_data = {
   "name": "Barbara",
   "age": 21
}

# Zaawansowane dane osobowe
advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# Tworzenie nowego słownika 'person' poprzez połączenie dwóch słowników
person = {**basic_data, **advanced_data}

# Wydrukowanie zawartości słownika 'person'
print("Zawartość słownika 'person':")
for key, value in person.items():
    print(f"{key}: {value}")
