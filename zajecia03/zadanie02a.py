imiona = ['Artur', 'Barbara', 'Czesław']

print(imiona)

indeks = int(input('Proszę podać indeks imienia do skasowania: '))

if indeks < len(imiona):
    print('Kasowane imię to:', imiona[indeks])
    del imiona[indeks]
else:
    print('Nie ma elementu o takim indeksie')

print(imiona)