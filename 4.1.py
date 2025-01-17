import queue

"""
Kolejka to struktura danych, która działa na zasadzie
First In, First Out (FIFO), czyli pierwszy element dodany
do kolejki będzie pierwszym, który zostanie usunięty.
Kolejka działa podobnie jak prawdziwa kolejka ludzi,
czekających na obsługę — osoba, która przyszła pierwsza,
będzie obsłużona pierwsza.
"""

# Tworzymy kolejkę
people = queue.Queue()

# Dodajemy elementy na koniec kolejki
people.put('Michael')  # Michael dołącza do kolejki
people.put('Charlotte')  # Charlotte dołącza do kolejki
people.put('Olivia')  # Olivia dołącza do kolejki

## Wypisanie liczby elementów w kolejce
print('Number of queue elements:', people.qsize())  # Zwraca liczbę elementów w kolejce

# Usuwamy i wypisujemy elementy z kolejki
while not people.empty():  # Dopóki kolejka nie jest pusta
    person = people.get()  # Usuwamy i pobieramy pierwszy element z kolejki
    print(person)  # Wypisujemy pobraną osobę
