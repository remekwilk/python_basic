gracze = [{'imie': 'Celina', 'wygrane': 12, 'przegrane': 3},
          {'imie': 'Barnaba', 'wygrane': 9, 'przegrane': 5},
          {'imie': 'Danuta', 'wygrane': 6, 'przegrane': 6},
          {'imie': 'Alojzy', 'wygrane': 5, 'przegrane': 7}]


def lista_imion_graczy(posortowane=False):
    imiona = []
    for gracz in gracze:
        imiona.append(gracz['imie'])

    if posortowane:
        return sorted(imiona)

    return imiona


lista = lista_imion_graczy(posortowane=True)
print(lista)
