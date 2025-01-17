import queue

# Tworzymy kolejkę plików do wydrukowania
files_to_print = queue.Queue()

# Pętla główna programu, która umożliwia użytkownikowi wybór akcji
while True:
    # Wyświetlamy menu
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':  # Jeśli użytkownik chce dodać plik do kolejki
        file_name = input('Enter file name to print: ')  # Wprowadzamy nazwę pliku
        # Dodajemy plik na koniec kolejki
        files_to_print.put(file_name)
    elif menu == '2':  # Jeśli użytkownik chce wydrukować plik
        if not files_to_print.empty():  # Sprawdzamy, czy kolejka nie jest pusta
            file_to_print = files_to_print.get()  # Pobieramy pierwszy plik z kolejki
            print(f'File {file_to_print} is currently being printed. Please wait!')  # Wypisujemy komunikat
        else:
            print('There are no files to print!')  # Jeśli kolejka jest pusta, informujemy użytkownika
    elif menu == '0':  # Jeśli użytkownik chce zakończyć program
        break  # Przerywamy pętlę i kończymy program
    else:
        raise ValueError('Input must be in (0, 1, 2)')  # Jeśli użytkownik wprowadził niewłaściwy wybór
