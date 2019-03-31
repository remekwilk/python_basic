from datetime import datetime

plik_do_zapisu = open('uruchomienia.log', mode='a')

teraz = datetime.now()
tekst = f'Skrypt został uruchomiony: {teraz}\n'
print(tekst)

plik_do_zapisu.write(tekst)
