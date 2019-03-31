# Uwaga, slice działa również na listach

tekst = 'Welcome! This is the documentation for Python 3.7.0.'

print(tekst[0])

# print(list(tekst))

print(tekst[9:13])

print(tekst[0:7])
print(tekst[:7])  # trochę krócej
print(tekst[7:])

print(tekst[:7] + tekst[7:])  # dostajemy KOPIĘ całego striga
print(tekst[:])  # również dostajemy KOPIĘ całego striga

print(tekst[-6:])

print(tekst[5:20:2])
