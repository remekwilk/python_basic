from random import sample


def chybil_trafil():
    liczby = sample(range(1, 20), k=4)
    return sorted(liczby)


def dodaj_zaklad(zaklad, wszystkie_zaklady):
    wszystkie_zaklady.append(zaklad)


def czy_jest_zwyciezca(zwycieskie_liczby, wszystkie_zaklady):
    if zwycieskie_liczby in wszystkie_zaklady:
        print(f'Mamy zwycięzcę I stopnia, który poprawnie skreślił liczby: {zwycieskie_liczby}')
    else:
        print('Tym razem nie ma zwycięzcy')
