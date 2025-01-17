import json

# Funkcja wczytująca dane z pliku JSON
def load_voting_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Jeśli plik nie istnieje, zwracamy pusty słownik

# Funkcja zapisująca dane do pliku JSON
def save_voting_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Główna część programu
if __name__ == "__main__":
    filename = "voting.json"

    # Wczytaj aktualne dane głosowania
    voting_data = load_voting_data(filename)

    # Pobierz nazwę osoby, na którą oddano głos
    person_name = input('Name of the person you are voting for: ').strip()

    # Zaktualizuj liczbę głosów
    if person_name in voting_data:
        voting_data[person_name] += 1
    else:
        voting_data[person_name] = 1

    # Zapisz zaktualizowane dane do pliku
    save_voting_data(filename, voting_data)

    # Wyświetl aktualne wyniki
    print("Updated voting results:")
    for name, votes in voting_data.items():
        print(f"{name}: {votes} votes")
