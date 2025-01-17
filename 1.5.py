# Lista krajów z ich populacją
countries = [
    {"name": "Poland", "population": 38000000},  # Polska - populacja
    {"name": "Germany", "population": 83000000},  # Niemcy - populacja
    {"name": "France", "population": 67000000},  # Francja - populacja
    {"name": "Italy", "population": 60000000},  # Włochy - populacja
    {"name": "Spain", "population": 47000000}   # Hiszpania - populacja
]

# Funkcja główna, która wyświetla tabelę krajów i ich populacji
def main():
    print("COUNTRY      POPULATION")  # Nagłówek tabeli
    for country in countries:  # Iteracja przez listę krajów
        # Wyświetlanie nazwy kraju i populacji w odpowiednim formacie
        print(f"{country['name']:<12} {country['population']}")

# Uruchomienie funkcji głównej, jeśli plik jest uruchamiany bezpośrednio
if __name__ == '__main__':
    main()
