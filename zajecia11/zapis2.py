nazwa_pliku = 'dane2.txt'

plik = open(nazwa_pliku, mode='a')

for i in range(10):
    tekst_do_zapisania = f'Linia numer {i}.\n'
    plik.write(tekst_do_zapisania)
