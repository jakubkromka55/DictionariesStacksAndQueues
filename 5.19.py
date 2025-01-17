import json

# Funkcja do załadowania danych z pliku
def load_reservations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

# Funkcja do obliczenia liczby pokoi
def count_rooms(reservations):
    return len(reservations)

# Funkcja do obliczenia liczby opłaconych rezerwacji
def count_paid_reservations(reservations):
    return sum(1 for reservation in reservations if reservation['paid'])

# Funkcja do obliczenia liczby nieopłaconych rezerwacji
def count_unpaid_reservations(reservations):
    return sum(1 for reservation in reservations if not reservation['paid'])

# Funkcja do obliczenia łącznej wartości opłaconych rezerwacji
def total_paid_value(reservations):
    return sum(reservation['price_per_night'] * reservation['nights'] for reservation in reservations if reservation['paid'])

# Funkcja do obliczenia łącznej wartości nieopłaconych rezerwacji
def total_unpaid_value(reservations):
    return sum(reservation['price_per_night'] * reservation['nights'] for reservation in reservations if not reservation['paid'])

# Funkcja do wyświetlenia podsumowania
def print_summary(reservations):
    print("Liczba pokoi:", count_rooms(reservations))
    print("Liczba opłaconych rezerwacji:", count_paid_reservations(reservations))
    print("Liczba nieopłaconych rezerwacji:", count_unpaid_reservations(reservations))
    print("Łączna wartość opłaconych rezerwacji: {:.2f} PLN".format(total_paid_value(reservations)))
    print("Łączna wartość nieopłaconych rezerwacji: {:.2f} PLN".format(total_unpaid_value(reservations)))

# Główna część programu
if __name__ == "__main__":
    file_path = 'reservations.json'
    reservations = load_reservations(file_path)
    print_summary(reservations)
