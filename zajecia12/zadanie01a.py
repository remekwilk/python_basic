from datetime import datetime

print('Uruchomienia do tej pory:')
try:
    plik_do_odczytu = open('uruchomienia.log', mode='r')
except FileNotFoundError:
    print('Brak historii uruchomień')
else:
    zawartosc = plik_do_odczytu.read()
    print(zawartosc)

plik_do_zapisu = open('uruchomienia.log', mode='a')
teraz = datetime.now()
tekst = f'Skrypt został uruchomiony: {teraz}\n'

print('Aktualne uruchomienie:')
print(tekst)
plik_do_zapisu.write(tekst)
