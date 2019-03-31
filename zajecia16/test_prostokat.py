import unittest
from prostokat import Prostokat

class TestProstokata(unittest.TestCase):
    def test_udaje_sie_utworzyc_prostokat(self):

        p = Prostokat(3, 5)

        oczekiwana = 3
        aktualna = p.bok_a
        self.assertEqual(oczekiwana, aktualna)

        self.assertEqual(5, p.bok_b)

    def test_repr_zwraca_dobry_opis(self):
        p = Prostokat(3, 5)

        oczekiwana = ''  # Wypełnij tę wartość aby test przechodził
        aktualna = p.__repr__()

        self.assertEqual(oczekiwana, aktualna)

    def test_pole_jest_obliczone_prawidlowo(self):
        pass  # napisz test, który sprawdzi, czy metoda pole() zwraca prawidłowy wynik







