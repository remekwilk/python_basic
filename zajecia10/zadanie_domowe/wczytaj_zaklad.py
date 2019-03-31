def wczytaj_zaklad():
    while True:
        wczytane = input('Wprowadź cztery różne liczby (każda od 1 do 19) oddzielone spacjami:\n')
        lista_liczb = wczytane.split()

        zaklad = []
        for element in lista_liczb:
            try:
                liczba = int(element)
            except ValueError:
                print(f'wartość "{element}" nie jest liczbą.')
                break

            if not 1 <= liczba <= 19:
                print(f'Liczba {liczba} nie należy do przedziału od 1 do 19.')
                break

            if liczba in zaklad:
                print(f'Liczba {liczba} powtórzyła się.')
                break

            zaklad.append(liczba)

        if len(zaklad) != 4:
            print('Wpisz zakład jeszcze raz.')
            continue

        return sorted(zaklad)


if __name__ == '__main__':
    zaklad = wczytaj_zaklad()
    print(zaklad)
