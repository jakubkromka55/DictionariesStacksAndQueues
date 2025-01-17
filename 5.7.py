# Funkcja zwraca listę nazw hoteli oddzielonych przecinkiem
def hotel_list(hotels):
    return ", ".join(hotel["name"] for hotel in hotels)

# Funkcja zwraca średnią cenę pokoi w danej liście hoteli, zaokrągloną do wartości całkowitej
def avg_price(hotels):
    return round(sum(hotel["price"] for hotel in hotels) / len(hotels))

# Dane hoteli w Krakowie
hotels_in_Krakow = [
   {"name": "Sky", "price": 320.00},
   {"name": "Metropol", "price": 480.00},
   {"name": "New Port", "price": 420.00},
   {"name": "Aparthotel", "price": 390.00}
]

# Dane hoteli w Sopocie
hotels_in_Sopot = [
   {"name": "Focus", "price": 510.00},
   {"name": "Aqua", "price": 345.00},
   {"name": "La Boutique", "price": 390.00},
   {"name": "Marina", "price": 410.00}
]

# Obliczanie i wyświetlanie wyników
krakow_hotels = hotel_list(hotels_in_Krakow)
krakow_avg = avg_price(hotels_in_Krakow)

sopot_hotels = hotel_list(hotels_in_Sopot)
sopot_avg = avg_price(hotels_in_Sopot)

print(f"Hotels in Krakow: {krakow_hotels}")
print(f"Average hotel price in Krakow: {krakow_avg}")
print(f"Hotels in Sopot: {sopot_hotels}")
print(f"Average hotel price in Sopot: {sopot_avg}")

# Porównanie cen
cheaper_city = "Krakow" if krakow_avg < sopot_avg else "Sopot"
print(f"Cheaper hotels in: {cheaper_city}")
