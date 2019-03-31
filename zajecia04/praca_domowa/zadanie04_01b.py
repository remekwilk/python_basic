skladniki = []

while True:
    liczba = int(input('Wpisz liczbę: '))

    if liczba < 0:
        continue

    skladniki.append(liczba)

    suma = sum(skladniki)

    print('Suma liczb', skladniki, 'to', suma)

    if suma > 100:
        break


