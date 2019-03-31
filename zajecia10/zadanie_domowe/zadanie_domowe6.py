from loteria_funkcje import chybil_trafil, dodaj_zaklad, czy_jest_zwyciezca

wszystkie_zaklady = []

moj_zaklad = [1, 2, 3, 4]
dodaj_zaklad(moj_zaklad, wszystkie_zaklady)

for i in range(100):
    losowy_zaklad = chybil_trafil()
    dodaj_zaklad(losowy_zaklad, wszystkie_zaklady)

print(wszystkie_zaklady)

zwycieskie_liczby = chybil_trafil()

print('Zwycięskie liczby to dziś:', zwycieskie_liczby)

czy_jest_zwyciezca(zwycieskie_liczby, wszystkie_zaklady)

if moj_zaklad == zwycieskie_liczby:
    print("HURRA! Moje liczby padły!")

