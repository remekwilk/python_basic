pytanie1 = input("Czy życzysz sobie kawy z mlekiem? [tak/nie]: ")

if pytanie1 == 'tak' or pytanie1 == 't':
    pytanie2 = input("Jakie mleko? [krowie/sojowe]: ")

    if pytanie2 == 'krowie' or pytanie2 == 'k':
        print("Wybrano kawę z mlekiem krowim")
    elif pytanie2 == 'sojowe' or pytanie2 == 's':
        print("Wybrano kawę z mlekiem sojowym")
    else:
        print("Nie rozumiem odpowiedzi ¯\_(ツ)_/¯")
elif pytanie1 == 'nie' or pytanie1 == 'n':
    print("Wybrano kawę czarną.")
else:
    print("Nie rozumiem odpowiedzi ¯\_(ツ)_/¯")