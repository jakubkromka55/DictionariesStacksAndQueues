# Funkcja obliczająca wynik wyrażenia RPN
def oblicz_rpn(wyrazenie):
    stos = []  # Stos, na którym będziemy przechowywać liczby i wyniki obliczeń
    
    # Dzielimy wyrażenie na części składające się z liczb i operatorów
    elementy = wyrazenie.split()

    # Przechodzimy po wszystkich elementach wyrażenia
    for element in elementy:
        if element.isdigit():  # Jeśli element jest liczbą
            stos.append(int(element))  # Dodajemy liczbę na stos
        elif element in ['+', '-', '*', '/']:  # Jeśli element jest operatorem
            # Zdejmujemy dwa elementy ze stosu, wykonujemy operację i wynik wkładamy na stos
            b = stos.pop()  # Pierwszy operand
            a = stos.pop()  # Drugi operand
            if element == '+':
                stos.append(a + b)
            elif element == '-':
                stos.append(a - b)
            elif element == '*':
                stos.append(a * b)
            elif element == '/':
                if b != 0:  # Sprawdzamy, czy nie dzielimy przez 0
                    stos.append(a / b)
                else:
                    print("Błąd: dzielenie przez 0")
                    return None
        elif element == '=':  # Jeżeli napotkamy znak '='
            if stos:
                return stos[-1]  # Zwracamy wynik, który znajduje się na szczycie stosu
            else:
                print("Błąd: brak wyniku do wyświetlenia")
                return None
        else:
            print(f"Błąd: nieznany element '{element}'")
            return None

# Przykłady użycia programu
wyrazenie1 = "2 3 + ="  # 2 + 3
wyrazenie2 = "2 4 1 + * ="  # 2 * (4 + 1)
wyrazenie3 = "2 3 + 4 5 + * ="  # (2 + 3) * (4 + 5)
wyrazenie4 = "8 3 1 + / 3 2 - 4 + * ="  # 8 / (3 + 1) * (3 - 2 + 4)

print(f"Wynik 1: {oblicz_rpn(wyrazenie1)}")
print(f"Wynik 2: {oblicz_rpn(wyrazenie2)}")
print(f"Wynik 3: {oblicz_rpn(wyrazenie3)}")
print(f"Wynik 4: {oblicz_rpn(wyrazenie4)}")
