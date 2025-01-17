mobile = {
    "OS": "Android",
    "brand": "Xiaomi",
    "model": "note 10 pro",
    "screen": "6'",
    "color": "black",
    "year": "2021"
}


def main():
    # Iteracja przez wszystkie klucze i wartości w słowniku 'mobile'
    for key, value in mobile.items():
        # Wyświetlenie klucza i odpowiadającej mu wartości w formacie "klucz : wartość"
        print(f"{key} : {value}")


if __name__ == '__main__':
    # Uruchomienie funkcji głównej, jeśli skrypt jest uruchamiany bezpośrednio
    main()
