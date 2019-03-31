from datetime import datetime

def wypisanie_historii():
    print('Uruchomienia do tej pory:')
    try:
        plik_do_odczytu = open('uruchomienia.log', mode='r')
    except FileNotFoundError:
        print('Brak historii uruchomień')
    else:
        zawartosc = plik_do_odczytu.read()
        print(zawartosc)

def zapisanie_uruchomienia():
    plik_do_zapisu = open('uruchomienia.log', mode='a')
    teraz = datetime.now()
    tekst = f'Skrypt został uruchomiony: {teraz}\n'

    print('Aktualne uruchomienie:')
    print(tekst)
    plik_do_zapisu.write(tekst)

if __name__ == '__main__':
    wypisanie_historii()
    zapisanie_uruchomienia()
