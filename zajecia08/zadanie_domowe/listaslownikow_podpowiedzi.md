# Zadanie "Lista słowników" - podpowiedzi

### Etap 1:
Funkcja musi wykorzystać pętlę `for` do przejścia po każdym elemencie listy `gracze`. Podczas jednej iteracji (jednego "obrotu") dla aktualnego elementu ma wypisać imię gracza. Jeśli elementem, na którym pętla obecnie się znajduje jest element `gracz` (jest to słownik), to aby wyciągnąć z niego imię należy napisać `gracz['imie']`.

### Etap 2:
Jest to modyfikacja etapu 1. Należy zadeklarować pustą listę wewnątrz funkcji. Następnie, zamiast wypisywać imię na ekran, należy dodać je do listy, za pomocą `lista.append(tutaj imie gracza)`. Ta funkcja zwraca wartość, więc po przejściu całej pętli uzyj wyrażenia `return`.

### Etap 3:
Kolejna funkcja wykorzystująca tę samą pętlę przechodzącą po wszystkich elementach listy `gracze`. Tym razem wewnątrz jednej iteracji, czyli dla jednego, konkretnego gracza trzba sprawdzić (używając instrukcji warunkowej `if`), czy jego imię (wyciągnięte tak jak w etapie 1) jest równe imieniu przekazanemu w parametrze do funkcji. Jeśli tak: wyciągamy jego wygrane i drukujemy na ekran. Jeśli nie, nie robimy nic (nie potrzeba nawet bluku `else`, po prostu kod nie wejdzie do bloku `if`). Imię z parametru i imię ze słownika porównujemy operatorem `==`.

### Etap 4:
Ponownie, przechodzimy po kolei po wszystkich graczach w pętli `for`. Dla każdego gracza musimy wykonać dwa sprawdzenia (dwie instrukcje `if`), jedno po drugim. Jeżeli jego imię to `zwycięzca`, to odczytujemy ilość jego zwycięstw `gracz['wygrane']`, dodajemy do tej wartości 1 i zapisujemy z powrotem. Jeżeli jego imię jest równe imieniu w argumencie `przegrany` to robimy to samo, ale z kluczem słownika `'przegrane'`.

### Etap 5:
W tym zadaniu nie używamy pętli. Jedyne, co trzeba zrobić, to wewnątrz funkcji stworzyć nowy słownik, w którym pod kluczem `'imię'` ustawiamy imię podane w argumencie funkcji, a pod pozostałymi kluczami ustawiamy wartość `0`. Tak stworzony słownik dodajemy do globalnie dostępnej listy `gracze` używając na tej liście metody `.append(tutaj nowy słownik)`.