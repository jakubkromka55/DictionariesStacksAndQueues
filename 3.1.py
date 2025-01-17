import queue

"""
Stos to struktura danych, która działa na zasadzie
Last In, First Out (LIFO), czyli ostatni element dodany
do stosu jest pierwszym, który zostaje usunięty.
Można to porównać do sterty talerzy — ostatni talerz
na wierzchu będzie pierwszym, który zdejmiesz.
"""

# Tworzenie stosu za pomocą LifoQueue
cards = queue.LifoQueue()

# Dodawanie elementów na wierzch stosu
cards.put('King of Hearts \u2665')  # Król Kier
cards.put('Queen of Diamonds \u2666')  # Królowa Kar
cards.put('Jack of Spades \u2660')  # Walet Pik

## Wypisanie liczby elementów w stosie
print('Number of stack elements:', cards.qsize())  # Zwraca liczbę elementów w stosie

# Usuwanie i wypisywanie elementów z wierzchu stosu
while not cards.empty():
    card = cards.get()  # Pobiera element z wierzchu stosu
    print(card)  # Wypisuje pobrany element

"""
Zwróć uwagę na kolejność wypisanych elementów.
Ostatni dodany element zostanie wydrukowany pierwszy.
"""

# Dodawanie liczb do stosu
cards.put(2)
cards.put(3)
cards.put(7)
cards.put(4)
cards.put(1)
cards.put(9)
cards.put(8)

# Funkcja obliczająca sumę dwóch ostatnich liczb ze stosu
def sum_last_two_numbers(cards):
    numbers = [cards.get() for _ in range(2)]  # Pobiera dwa ostatnie elementy ze stosu
    return sum(numbers)  # Zwraca ich sumę

# Funkcja obliczająca sumę wszystkich liczb w stosie
def sum_all_numbers(cards):
    total = 0  # Zmienna do sumowania
    while not cards.empty():  # Dopóki stos nie jest pusty
        card = cards.get()  # Pobiera element ze stosu
        total += card  # Dodaje wartość do sumy
    return total  # Zwraca całkowitą sumę

# Wyświetlenie wyników sumowania
print()
print('Sum of last two numbers:', sum_last_two_numbers(cards))  # Suma dwóch ostatnich liczb
print('Sum of the rest:', sum_all_numbers(cards))  # Suma pozostałych liczb
