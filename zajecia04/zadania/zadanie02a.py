while True:
    odpowiedz = input('Wpisz wyraz: ')

    if odpowiedz == '':
        break

    if ' ' in odpowiedz:
        print('Znaleziono spację w wyrazie, wpisz ponownie.')
        continue

    print('Wpisany wyraz ma długość', len(odpowiedz), 'znaków.')
