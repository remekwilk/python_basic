class Prostokat:
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b

    def __repr__(self):
        return f'Prostokąt o bokach {self.bok_a} i {self.bok_b}'

    def pole(self):
        return self.bok_a * self.bok_b


if __name__ == '__main__':
    p = Prostokat(5, 9)
    print(p)
    print(p.pole())
