import queue

INPUT = 18  # Wartość liczby dziesiętnej do konwersji

# Funkcja konwertująca liczbę dziesiętną na liczbę binarną
def convert_to_binary(decimal):
    stack = queue.LifoQueue()  # Tworzymy stos (LifoQueue) do przechowywania reszt
    dec_to_bin(decimal, stack)  # Wywołanie rekurencyjnej funkcji konwertującej

    output = list()  # Lista do przechowywania wynikowego ciągu binarnego
    while not stack.empty():
        bin_value = stack.get()  # Pobieramy wartość z wierzchu stosu
        output.append(bin_value)  # Dodajemy ją do listy wynikowej

    return ''.join(map(str, output))  # Łączymy listę w ciąg i zwracamy jako wynik

# Funkcja rekurencyjna konwertująca liczbę dziesiętną na binarną
def dec_to_bin(dec: int, stack: queue.LifoQueue):
    if dec == 0:  # Bazowy przypadek - jeśli liczba wynosi 0, dodajemy 0 do stosu
        stack.put(0)
    elif dec == 1:  # Jeśli liczba wynosi 1, dodajemy 1 do stosu
        stack.put(1)
    else:
        stack.put(dec % 2)  # Dodajemy resztę z dzielenia przez 2 (0 lub 1) do stosu
        return dec_to_bin(dec // 2, stack)  # Rekurencyjne wywołanie dla liczby dzielonej przez 2

# Funkcja główna
def main():
    print('Natural number: ', INPUT)  # Wypisujemy liczbę dziesiętną
    print('Binary number: ', convert_to_binary(INPUT))  # Wypisujemy liczbę binarną

# Wywołanie funkcji głównej, jeśli skrypt jest uruchomiony bezpośrednio
if __name__ == '__main__':
    main()
