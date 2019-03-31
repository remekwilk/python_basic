while True:
    wyraz = input('Wpisz dowolne wyraz: ')

    ile_znakow = len(wyraz)

    komunikat = 'Wyraz "{}" ma {} znaków.\n' \
                'Wyraz ten zaczyna się na literę "{}"'.format(wyraz,
                                                              ile_znakow,
                                                              wyraz[0])

    print(komunikat)
