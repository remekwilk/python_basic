gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]


def ile_razy_wygral(imie):
    for gracz in gracze:
        if gracz['imie'] == imie:
            wygrane = gracz['wygrane']
            print(f'Gracz "{imie}" wygrał(a) {wygrane} gier.')


ile_razy_wygral('Barnaba')
