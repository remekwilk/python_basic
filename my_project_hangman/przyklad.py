import os
import random
import string

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     | 
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  |-+-
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  |-+-|
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  |-+-|
     |    |
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  |-+-|
     |    |
     |    |
     |   | 
     |   | 
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  |-+-|
     |  | | |
     |    |
     |   | |
     |   | |
     |  
    ----------
    """)


def menu():
    print('░' * 88)
    print('''
    
            ##      ## ####  ######  #### ######## ##       ########  ######  
            ##  ##  ##  ##  ##    ##  ##  ##       ##       ##       ##    ## 
            ##  ##  ##  ##  ##        ##  ##       ##       ##       ##       
            ##  ##  ##  ##   ######   ##  ######   ##       ######   ##       
            ##  ##  ##  ##        ##  ##  ##       ##       ##       ##       
            ##  ##  ##  ##  ##    ##  ##  ##       ##       ##       ##    ## 
             ###  ###  ####  ######  #### ######## ######## ########  ######                                                                                              
        ''')
    print('░' * 88)
    while True:
        znak = input('                            NEW GAME: [N]    EXIT: [Q]\n')
        if znak in 'nN':
            return nowa_gra()
        if znak in 'qQ':
            exit()
        else:
            pass


def nowa_gra():
    haslo = losowanie_slowa()
    gra(haslo)


def losowanie_slowa():
    clear()
    plik = open('words.txt', mode='r')
    zawartosc = plik.read().split()
    haslo = random.choice(zawartosc)
    return haslo


def wyswietlanie_hasla(haslo, lista_liter):
    do_druku = '    '
    flaga = True

    for znak in haslo:
        if znak in lista_liter:
            do_druku += znak
        else:
            do_druku += '░'
            flaga = False
        do_druku += ' '

    print(f'\nHasło do odgadnięcia ma {len(haslo)} liter: {do_druku}')
    if flaga:
        return wygrana(haslo)


def wczytywanie_znaku(haslo):
    while True:
        litera = input('Podaj literę: ')
        if len(litera) > 1:
            if litera == haslo:
                return wygrana(haslo)
        if litera in string.ascii_letters:
            litera = litera.lower()
        else:
            print('Podałeś zły znak!')
            continue
        return litera


def wygrana(haslo):
    print(f'\nGratulacje, odgadłeś wyraz {haslo}\n')
    input('Aby powrócić do menu ENTER')
    clear()
    menu()


def gra(haslo):
    odgadniete = []
    ilosc_prob = 0
    maksymalna_ilosc_prob = len(HANGMAN) - 1

    while True:
        wyswietlanie_hasla(haslo, odgadniete)
        print(haslo)
        znak = wczytywanie_znaku(haslo)

        if znak in haslo:
            odgadniete.append(znak)
        else:
            ilosc_prob += 1
            if ilosc_prob == maksymalna_ilosc_prob:
                print('\nZostałeś powieszony!')
                print(HANGMAN[ilosc_prob])
                print(f'Szukany wyraz to "{haslo}" ')
                input('Nacisnij Enter aby wrócić do MENU')
                clear()
                menu()
            else:
                print(HANGMAN[ilosc_prob])


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return


menu()
