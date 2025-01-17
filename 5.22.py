import json

# Tworzymy pusty słownik, który będzie przechowywał dane produktu
product = {}

# Pobieranie danych od użytkownika
product["name"] = input("Podaj nazwę produktu: ")  # Nazwa produktu (string)
product["price"] = float(input("Podaj cenę produktu (liczba zmiennoprzecinkowa, np. 12.99): "))  # Cena (float)
paid_input = input("Czy zapłacono? (tak/nie): ").strip().lower()  # Zapytanie o zapłatę

# Zamieniamy odpowiedź "tak" na True, a "nie" na False
if paid_input == "tak":
    product["paid"] = True
elif paid_input == "nie":
    product["paid"] = False
else:
    print("Błędna odpowiedź! Zakładam, że nie zapłacono.")
    product["paid"] = False

# Ścieżka do pliku, do którego zapisujemy dane
file_name = "product.json"

# Zapisujemy dane do pliku JSON
with open(file_name, 'w') as file:
    json.dump(product, file, indent=4)

print(f"Dane zostały zapisane do pliku {file_name}")
