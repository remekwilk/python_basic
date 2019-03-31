liczba = int(input('Podaj liczbę naturalną: '))

wszystkie_dzielniki = []

for dzielnik in range(1, liczba + 1):
    if liczba % dzielnik == 0:
        wszystkie_dzielniki.append(dzielnik)

print('Dzieliniki liczby', liczba, 'to:', wszystkie_dzielniki)

if len(wszystkie_dzielniki) == 2:
    print('Liczba', liczba, 'jest liczbą pierwszą!')
