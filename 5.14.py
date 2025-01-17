from collections import deque

class BiuroObslugi:
    def __init__(self):
        self.kolejka = deque()  # Inicjalizacja pustej kolejki
        self.numer_biletu = 1    # Inicjalizacja numeru biletu

    def przyjmij_klienta(self, imie):
        """
        Funkcja przyjmuje nowego klienta i przypisuje mu numer biletu,
        a następnie dodaje go do kolejki.
        """
        klient = {'imie': imie, 'numer_biletu': self.numer_biletu}
        self.kolejka.append(klient)  # Dodajemy klienta na koniec kolejki
        print(f"Klient {imie} otrzymał bilet o numerze {self.numer_biletu}")
        self.numer_biletu += 1  # Zwiększamy numer biletu na kolejnego klienta

    def obsluz_klienta(self):
        """
        Funkcja obsługuje pierwszego klienta w kolejce.
        Jeśli kolejka jest pusta, wyświetla komunikat o braku klientów.
        """
        if self.kolejka:
            klient = self.kolejka.popleft()  # Zdejmujemy klienta z początku kolejki
            print(f"Obsługuję klienta: {klient['imie']} z biletem nr {klient['numer_biletu']}")
        else:
            print("Brak klientów w kolejce.")

    def wyswietl_kolejke(self):
        """
        Funkcja wyświetla wszystkich klientów czekających w kolejce.
        """
        if self.kolejka:
            print("Klienci w kolejce:")
            for klient in self.kolejka:
                print(f"{klient['imie']} (Bilet nr {klient['numer_biletu']})")
        else:
            print("Kolejka jest pusta.")

# Przykładowe użycie programu:
biuro = BiuroObslugi()

# Przyjmowanie klientów
biuro.przyjmij_klienta("Anna")
biuro.przyjmij_klienta("Marek")
biuro.przyjmij_klienta("Jan")

# Wyświetlanie kolejki
biuro.wyswietl_kolejke()

# Obsługa klientów
biuro.obsluz_klienta()  # Obsługuje Annę
biuro.obsluz_klienta()  # Obsługuje Marka
biuro.obsluz_klienta()  # Obsługuje Jana

# Sprawdzanie kolejki po obsłużeniu klientów
biuro.wyswietl_kolejke()
