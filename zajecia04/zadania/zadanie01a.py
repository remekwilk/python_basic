liczba = int(input('Podaj liczbę naturalną: '))

for dzielnik in range(1, liczba + 1):
    if liczba % dzielnik == 0:
        print(liczba, 'jest podzielna przez', dzielnik)
