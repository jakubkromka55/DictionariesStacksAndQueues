import json

# Słownik opisujący ulubioną książkę
favorite_book = {
    "title": "Harry Potter i Kamień Filozoficzny",
    "author": "J.K. Rowling",
    "genre": "Fantasy",
    "publication_year": 1997,
    "rating": 4.9,
    "language": "Polish"
}

# Ścieżka do pliku
file_name = "favorite.json"

# Otwarcie pliku w trybie zapisu i zapisanie słownika w formacie JSON
with open(file_name, 'w') as file:
    json.dump(favorite_book, file, indent=4)

print(f"Data has been written to {file_name}")
