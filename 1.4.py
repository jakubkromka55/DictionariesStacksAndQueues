# Utworzenie słownika z danymi osoby
person = {
   "name": "Marek",  # Imię
   "surname": "Banach",  # Nazwisko
   "age": 25,  # Wiek
   "hobby": ["swimming", "excursions"],  # Lista hobby
   "married": True,  # Status małżeński (prawda/fałsz)
   "phone": {  # Słownik z numerami telefonów
       "landline": "123444321",  # Telefon stacjonarny
       "mobile": "777888999"  # Telefon komórkowy
   }
}

# Wyświetlanie imienia osoby
print("Imię:", person["name"])

# Wyświetlanie hobby osoby
print("Hobby:", person["hobby"])

# Wyświetlanie całej zawartości słownika
print("Cała zawartość słownika:", person)

# Zmiana nazwiska na "Nowak"
person["surname"] = "Nowak"

# Zmiana statusu małżeńskiego na przeciwny
person["married"] = not person["married"]

# Dodanie płci: "mężczyzna"
person["gender"] = "mężczyzna"

# Dodanie nowego hobby: "rower"
person["hobby"].append("rower")

# Dodanie telefonu służbowego
person["phone"]["work"] = "313131444"

# Wyświetlanie całej zawartości słownika po zmianach
print("Zaktualizowana zawartość słownika:")
for key, value in person.items():
    print(f"{key}: {value}")
