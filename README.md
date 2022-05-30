# prosta_biblioteka

Na wejściu w pierwszej linijce podana jest liczba akcji (n).
W kolejnych linijkach podane są akcje:
    ○ dodaj – oznacza dodanie książki do biblioteki, zapisane np. jako :
("dodaj", "Pan Tadeusz", "Adam Mickiewicz", 2000)
    ○ wypozycz – oznacza wypożyczenie egzemplarza ksiazki przez
czytelnika (można wypożyczyć tylko jeden egzemplarz tej samej
książki; przyjmij też, że domyślnie można wypożyczyć maksymalnie 3
egzemplarze różnych książek). Akcja może być zapisana jako:
("wypozycz", "Jakub Dzikowski", "Quo Vadis")
    ○ oddaj – oznacza zwrócenie konkretnego egzemplarza książki do
biblioteki. Może być zapisane jako : ("oddaj", "Jakub Dzikowski", "Quo
Vadis")

### Przykładowe wejście:
12
("dodaj", "Pan Tadeusz", "Adam Mickiewicz", 2000)
("dodaj", "Quo Vadis", "Henryk Sienkiewicz", 2010)
("dodaj", "Chatka Puchatka", "Alan Alexander Milne", 1998)
("dodaj", "Pan Tadeusz", "Adam Mickiewicz", 2000)
("dodaj", "Chatka Puchatka", " Alan Alexander Milne", 2014)
("wypozycz", "Bartek Perkowski", "Pan Tadeusz")
("wypozycz", "Bartek Perkowski", "Pan Tadeusz")
("wypozycz", "Jacek Malyszko", "Quo Vadis")
("wypozycz", "Bartek Perkowski", "Quo Vadis")
("oddaj", "Jacek Malyszko", "Quo Vadis")
("wypozycz", "Bartek Perkowski", "Quo Vadis")
("oddaj", "Jacek Malyszko", "Quo Vadis")