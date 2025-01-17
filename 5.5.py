# Program zlicza, ile razy każde słowo pojawia się w akapicie.

paragraph = "cat dog mouse cat rat cat mouse"

# Podział akapitu na pojedyncze słowa (zwraca listę słów)
words = paragraph.split()

# Tworzymy pusty słownik do przechowywania liczby wystąpień słów
word_count = {}

# Iterujemy przez każde słowo w liście
for word in words:
    # Jeśli słowo już jest w słowniku, zwiększamy licznik
    if word in word_count:
        word_count[word] += 1
    else:
        # Jeśli słowa nie ma w słowniku, dodajemy je z wartością 1
        word_count[word] = 1

# Wyświetlenie wyników
for word, count in word_count.items():
    print(f"'{word}' występuje {count} raz(y).")
