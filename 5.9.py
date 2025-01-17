import csv

# Wczytaj dane z pliku province.csv i utwórz słownik {litera: województwo}
def load_province_mapping(filename):
    province_mapping = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pomijamy nagłówek
        for row in reader:
            letter, name = row
            province_mapping[letter] = name
    return province_mapping

# Wczytaj numery rejestracyjne z pliku vehicle.txt
def load_vehicle_data(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        return [line.strip() for line in file]

# Oblicz liczbę samochodów zarejestrowanych w każdym województwie
def count_vehicles_by_province(vehicle_data, province_mapping):
    province_count = {name: 0 for name in province_mapping.values()}
    for vehicle in vehicle_data:
        if vehicle[0] in province_mapping:
            province_name = province_mapping[vehicle[0]]
            province_count[province_name] += 1
    return province_count

# Główna część programu
if __name__ == "__main__":
    province_mapping = load_province_mapping("province.csv")
    vehicle_data = load_vehicle_data("vehicle.txt")
    province_counts = count_vehicles_by_province(vehicle_data, province_mapping)

    # Wyświetlenie wyników
    print("Liczba samochodów zarejestrowanych w poszczególnych województwach:")
    for province, count in province_counts.items():
        print(f"{province}: {count}")
