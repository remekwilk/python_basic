from random import sample


def chybil_trafil():
    liczby = sample(range(1, 20), k=4)
    return sorted(liczby)


zaklad = chybil_trafil()

print(zaklad)
