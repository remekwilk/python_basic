pytanie1 = input("Czy życzysz sobie kawy z mlekiem? [tak/nie]: ")

if pytanie1 == 'tak' or pytanie1 == 't':
    pytanie2 = input("Jakie mleko? [krowie/sojowe]: ")

    if pytanie2 == 'krowie' or pytanie2 == 'k':
        wybrana_kawa = "Wybrano kawę z mlekiem krowim"
    elif pytanie2 == 'sojowe' or pytanie2 == 's':
        wybrana_kawa = "Wybrano kawę z mlekiem sojowym"
    else:
        print("Nie rozumiem odpowiedzi ¯\_(ツ)_/¯")
        exit()
elif pytanie1 == 'nie' or pytanie1 == 'n':
    wybrana_kawa = "Wybrano kawę bez mleka"  # małe dopasowanie, aby było gramatycznie :)
else:
    print("Nie rozumiem odpowiedzi ¯\_(ツ)_/¯")
    exit()

pytanie3 = input("Czy dodać cukier? [tak/nie]")
if pytanie3 == 'tak' or pytanie3 == 't':
    wybrana_kawa = wybrana_kawa + ' z cukrem.'
elif pytanie3 == 'nie' or pytanie3 == 'n':
    wybrana_kawa = wybrana_kawa + ' bez cukru.'
else:
    print("Nie rozumiem odpowiedzi ¯\_(ツ)_/¯")
    exit()

print(wybrana_kawa)