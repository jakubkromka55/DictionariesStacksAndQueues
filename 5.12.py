# Funkcja odwracająca ciąg za pomocą stosu
def reverse_string_with_stack(input_string):
    stack = []  # Stos do przechowywania znaków

    # Dodanie każdego znaku na stos
    for char in input_string:
        stack.append(char)

    # Pobieranie znaków ze stosu i tworzenie odwróconego ciągu
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Główna część programu
if __name__ == "__main__":
    # Pobranie tekstu od użytkownika
    user_input = input("Enter a string to reverse: ").strip()

    # Odwrócenie ciągu
    reversed_text = reverse_string_with_stack(user_input)

    # Wyświetlenie odwróconego tekstu
    print(f"Reversed string: {reversed_text}")
