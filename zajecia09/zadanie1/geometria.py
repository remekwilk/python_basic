WARTOSC_PI = 3.14


def pole_prostokata(a, b):
    if a < 0 or b < 0:
        return None
    return a * b


def pole_kola(r):
    if r < 0:
        return None
    return WARTOSC_PI * r ** 2
