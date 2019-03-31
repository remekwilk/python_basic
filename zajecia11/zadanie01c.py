from datetime import datetime

while True:
    data_z_klawiatury = input("Podaj datę urodzin (w formacie RRRR-MM-DD): ")
    try:
        data_urodzin = datetime.strptime(data_z_klawiatury, '%Y-%m-%d')
    except ValueError:
        print('Podana data nie była w formacie RRRR-MM-DD.')
    else:
        break

obecna_data = datetime.now()

roznica = obecna_data - data_urodzin

lata = roznica.days // 365
dni = roznica.days % 365
print('Osoba ma obecnie: {} lat i {} dni'.format(lata, dni))
