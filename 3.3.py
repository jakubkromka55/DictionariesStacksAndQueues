import queue

# Przykłady wyrażeń do sprawdzenia poprawności nawiasów
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # Nawiasy są poprawne
expression2 = "[(2+3]/4)"  # Nawiasy niepoprawne
expression3 = "(2-3*4+(5/6)"  # Nawiasy niepoprawne

# Mapowanie nawiasów otwierających i zamykających
bracket_map = {
    '[': ']',
    '(': ')',
    '{': '}'
}

# Funkcja sprawdzająca poprawność nawiasów w wyrażeniu
def brackets_ok(expression):
    brackets = queue.LifoQueue()  # Tworzymy stos do przechowywania nawiasów otwierających
    for element in expression:
        # Jeśli element jest nawiasem otwierającym, dodajemy go do stosu
        if element in ['[', '(', '{']:
            brackets.put(element)
        # Jeśli element jest nawiasem zamykającym
        elif element in [']', ')', '}']:
            if brackets.empty():  # Jeśli stos jest pusty, oznacza, że nie ma nawiasu otwierającego
                return False
            opening_bracket = brackets.get()  # Pobieramy nawias otwierający ze stosu
            # Sprawdzamy, czy nawiasy się zgadzają
            if not bracket_map[opening_bracket] == element:
                return False
    # Jeśli po przetworzeniu całego wyrażenia stos jest pusty, oznacza to, że wszystkie nawiasy zostały poprawnie zamknięte
    return brackets.empty()

# Sprawdzanie poprawności nawiasów dla każdego z wyrażeń
for expression in [expression1, expression2, expression3]:
    if brackets_ok(expression):
        print(f'expression {expression} is valid')  # Nawiasy poprawne
    else:
        print(f'expression {expression} is invalid')  # Nawiasy niepoprawne
