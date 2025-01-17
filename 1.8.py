# Poczatkowa lista cen
price_list = {
    'T-shirt': 19.99,  # Koszulka - cena
    'Jeans': 49.99,  # Dżinsy - cena
    'Jacket': 89.99,  # Kurtka - cena
    'Sneakers': 59.99,  # Buty sportowe - cena
    'Hat': 15.99  # Czapka - cena
}

# Funkcja wyświetlająca produkty i ich ceny przed rabatem
def before_discount():
    print("Produkty i ceny przed rabatem:")
    for product, price in price_list.items():  # Iteracja przez listę cen
        print(f"{product}: ${price:.2f}")

# Funkcja wyświetlająca łączną wartość produktów przed rabatem
def before_discount_total():
    total_before_discount = sum(price_list.values())  # Sumowanie cen
    print(f"\nŁączna wartość produktów przed rabatem: ${total_before_discount:.2f}")

# Funkcja nakładająca 10% rabatu na wszystkie produkty
def apply_discount():
    for product in price_list:  # Iteracja przez produkty
        price_list[product] = round(price_list[product] * 0.9, 2)  # Obniżenie ceny o 10%

# Funkcja wyświetlająca produkty i ich ceny po rabacie
def after_discount():
    print("\nProdukty i ceny po 10% rabacie:")
    for product, price in price_list.items():  # Iteracja przez listę cen po rabacie
        print(f"{product}: ${price:.2f}")

# Funkcja wyświetlająca łączną wartość produktów po rabacie
def after_discount_total():
    total_after_discount = sum(price_list.values())  # Sumowanie cen po rabacie
    print(f"\nŁączna wartość produktów po rabacie: ${total_after_discount:.2f}")

# Funkcja główna wywołująca wszystkie kroki

def main():
    before_discount()  # Wyświetlenie cen przed rabatem
    before_discount_total()  # Wyświetlenie łącznej ceny przed rabatem
    apply_discount()  # Zastosowanie rabatu
    after_discount()  # Wyświetlenie cen po rabacie
    after_discount_total()  # Wyświetlenie łącznej ceny po rabacie

# Uruchomienie funkcji głównej, jeśli plik jest uruchamiany bezpośrednio
if __name__ == '__main__':
    main()
