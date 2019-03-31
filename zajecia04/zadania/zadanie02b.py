while True:
    odpowiedz = input('Wpisz wyraz: ')

    if not odpowiedz:  # Popularny 'skrót' w Pythonie
        break

    odpowiedz = odpowiedz.strip()

    if ' ' in odpowiedz:
        print('Znaleziono spację w wyrazie, wpisz ponownie.')
        continue

    print('Wpisany wyraz ma długość', len(odpowiedz), 'znaków.')
