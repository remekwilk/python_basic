class Plecak:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.kolor = 'zielony'

    def __repr__(self):
        return f'Plecak koloru {self.kolor} o pojemności {self.pojemnosc}l.'
