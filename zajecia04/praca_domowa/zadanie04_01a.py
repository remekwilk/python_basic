suma = 0
skladniki = []

while suma < 100:
    liczba = int(input('Wpisz liczbę:'))

    skladniki.append(liczba)
    suma = suma + liczba

    print('Suma liczb', skladniki, 'to', suma)
