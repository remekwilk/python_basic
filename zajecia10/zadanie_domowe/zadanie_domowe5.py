from loteria_funkcje import chybil_trafil, dodaj_zaklad, czy_jest_zwyciezca

wszystkie_zaklady = []

print(wszystkie_zaklady)

moj_zaklad = [1, 2, 3, 4]
dodaj_zaklad(moj_zaklad, wszystkie_zaklady)

for i in range(10):
    losowy_zaklad = chybil_trafil()
    dodaj_zaklad(losowy_zaklad, wszystkie_zaklady)

print(wszystkie_zaklady)

czy_jest_zwyciezca([1, 2, 3, 4], wszystkie_zaklady)
