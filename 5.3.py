# Słownik z tłumaczeniami
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

# Pętla, która umożliwia wprowadzenie słowa przez użytkownika
while True:
    # Użytkownik wprowadza słowo po angielsku
    word = input("Enter an English word to translate (or type 'exit' to quit): ").lower()

    if word == 'exit':  # Jeśli użytkownik wpisze 'exit', program zakończy działanie
        print("Exiting the program.")
        break

    # Sprawdzamy, czy słowo znajduje się w słowniku
    if word in translations:
        print(f"The translation of '{word}' is: {translations[word]}")  # Wyświetlamy tłumaczenie
    else:
        print(f"Sorry, translation for '{word}' is not available.")  # Tłumaczenie niedostępne
