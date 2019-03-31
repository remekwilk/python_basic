gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]


def dodaj_gre(zwyciezca, przegrany):
    for gracz in gracze:
        if gracz['imie'] == zwyciezca:
            gracz['wygrane'] += 1
        if gracz['imie'] == przegrany:
            gracz['przegrane'] += 1


dodaj_gre(zwyciezca='Alojzy', przegrany='Celina')

print(gracze)
