import queue

# Tworzymy stos (LifoQueue), który będzie przechowywał odwiedzone strony
visited_websites = queue.LifoQueue()

# Przykładowe wcześniej odwiedzone strony
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

# Pętla, która umożliwia użytkownikowi poruszanie się po historii odwiedzanych stron
while True:
    # Użytkownik wprowadza nazwę strony
    website = input('Enter website name (0 for back): ')

    # Jeśli użytkownik wprowadzi '0', wracamy do poprzedniej odwiedzonej strony
    if website == '0':
        if visited_websites.empty():  # Jeśli stos jest pusty, oznacza to brak historii
            break  # Przerywamy pętlę, kończymy działanie programu
        else:
            print('<-- Going back to a previously visited website')  # Informujemy użytkownika, że wracamy
            website = visited_websites.get()  # Pobieramy stronę z wierzchu stosu (ostatnio odwiedzona)
    elif website != "":  # Jeśli użytkownik wprowadził poprawną nazwę strony (nie pustą)
        visited_websites.put(website)  # Dodajemy stronę do historii
    else:
        raise ValueError('Website cannot be empty')  # Jeśli użytkownik nie wprowadził żadnej nazwy strony, zgłaszamy błąd

    # Wyświetlamy stronę, którą użytkownik aktualnie przegląda
    print('You are currently viewing:', website)
    print()
