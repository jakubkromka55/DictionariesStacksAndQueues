# Słownik zawierający produkty i ich ilości w magazynie
store_inventory = {
    'Laptop': 15, 
    'Desktop PC': 10, 
    'Monitor': 25,  
    'Keyboard': 50,  
    'Mouse': 60,  
    'External Hard Drive': 30,  
    'Printer': 12,  
    'Router': 20,  
    'USB Flash Drive': 100,  
    'Graphics Card': 8  
}

# Funkcja główna, która wyświetla listę produktów, ich ilości oraz łączną liczbę produktów

def main():
    print("Lista produktów i ich ilości:")
    for product, quantity in store_inventory.items():  # Iteracja przez produkty w magazynie
        print(f"{product}: {quantity}")  # Wyświetlenie nazwy produktu i jego ilości

    # Obliczenie łącznej liczby produktów
    total_products = sum(store_inventory.values())
    print(f"\nŁączna liczba produktów w magazynie: {total_products}")

# Uruchomienie funkcji głównej, jeśli plik jest uruchamiany bezpośrednio
if __name__ == '__main__':
    main()
