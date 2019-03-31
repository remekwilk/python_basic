print('Uruchomienia do tej pory:')

plik_do_odczytu = open('uruchomienia.log', mode='r')
zawartosc = plik_do_odczytu.read()
print(zawartosc)
