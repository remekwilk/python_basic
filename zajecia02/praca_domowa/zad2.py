pytanie1 = input("Czy życzysz sobie kawy z mlekiem? [tak/nie]: ")

if pytanie1 == 'tak':
    pytanie2 = input("Jakie mleko? [krowie/sojowe]: ")

    if pytanie2 == 'krowie':
        print("Wybrano kawę z mlekiem krowim")
    elif pytanie2 == 'sojowe':
        print("Wybrano kawę z mlekiem sojowym")
    else:
        print("Nie rozumiem odpowiedzi ¯\_(ツ)_/¯")
elif pytanie1 == 'nie':
    print("Wybrano kawę czarną.")
else:
    print("Nie rozumiem odpowiedzi ¯\_(ツ)_/¯")