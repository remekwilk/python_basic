import json

dane_json = '[{"nazwa": "jab\u0142ko", "cena": 2.49, "czy_na_sztuki": false}, {"nazwa": "kiwi", "cena": 23.9, "czy_na_sztuki": false}, {"nazwa": "figa", "cena": 3.49, "czy_na_sztuki": true}, {"nazwa": "pomidor", "cena": 7.49, "czy_na_sztuki": false}, {"nazwa": "arbuz", "cena": 3.99, "czy_na_sztuki": false}, {"nazwa": "cytryna", "cena": 6.99, "czy_na_sztuki": false}, {"nazwa": "awokado", "cena": 4.99, "czy_na_sztuki": true}]'

dane = json.loads(dane_json)

print(dane)
print(type(dane))

print(dane[0]['nazwa'])
