imiona = ['Artur', 'Barbara', 'Czesław']

print(imiona)

indeks = int(input('Proszę podać indeks imienia do skasowania: '))

indeks_min = -1 * len(imiona)
indeks_max = len(imiona) -1

if  indeks_min <= indeks <= indeks_max :
    print('Kasowane imię to:', imiona.pop(indeks))
else:
    print('Nie ma elementu o takim indeksie')

print(imiona)