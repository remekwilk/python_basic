from random import sample


def chybil_trafil():
    liczby = sample(range(1, 20), k=4)
    return sorted(liczby)


wszystkie_zaklady = []


def dodaj_zaklad(zaklad):
    wszystkie_zaklady.append(zaklad)


print(wszystkie_zaklady)

moj_zaklad = [1, 2, 3, 4]
dodaj_zaklad(moj_zaklad)

for i in range(10):
    losowy_zaklad = chybil_trafil()
    dodaj_zaklad(losowy_zaklad)

print(wszystkie_zaklady)
