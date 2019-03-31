from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik


class Druzyna:
    def __init__(self):
        self.wojownicy = []

    def dodaj_wojownika(self, wojownik):
        self.wojownicy.append(wojownik)

    def marsz(self, dystans):
        for wojownik in self.wojownicy:
            wojownik.maszeruj(dystans)

    def atak(self):
        for wojownik in self.wojownicy:
            wojownik.atakuj()

    def raport(self):
        ile_wojownikow = len(self.wojownicy)
        print('W drużynie jest {} wojowników:'.format(ile_wojownikow))
        for wojownik in self.wojownicy:
            print(wojownik)


if __name__ == '__main__':
    d = Druzyna()

    r = Rycerz()
    d.dodaj_wojownika(r)

    # nie musimy tworzyć zmiennej
    d.dodaj_wojownika(Lucznik())

    d.marsz(1000)

    d.raport()


