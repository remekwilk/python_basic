gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]


def dodaj_gracza(imie):
    nowy_gracz = {'imie': imie,
                  'wygrane': 0,
                  'przegrane': 0}

    gracze.append(nowy_gracz)


dodaj_gracza('Xavier')

print(gracze)
