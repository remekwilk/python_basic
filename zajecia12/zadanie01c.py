from datetime import datetime


def wypisanie_historii():
    print('Uruchomienia do tej pory:')
    try:
        with open('uruchomienia.log', mode='r') as plik_do_odczytu:
            zawartosc = plik_do_odczytu.read()
            print(zawartosc)
    except FileNotFoundError:
        print('Brak historii uruchomień')


def zapisanie_uruchomienia():
    with open('uruchomienia.log', mode='a') as plik_do_zapisu:
        teraz = datetime.now()
        tekst = f'Skrypt został uruchomiony: {teraz}\n'

        print('Aktualne uruchomienie:')
        print(tekst)
        plik_do_zapisu.write(tekst)


if __name__ == '__main__':
    wypisanie_historii()
    zapisanie_uruchomienia()
