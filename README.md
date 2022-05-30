# prosta biblioteka

Na wejściu w pierwszej linijce podana jest liczba akcji (n).
W kolejnych linijkach podane są akcje:<br>
    - dodaj – oznacza dodanie książki do biblioteki, zapisane np. jako :
("dodaj", "Pan Tadeusz", "Adam Mickiewicz", 2000)<br>
    - wypozycz – oznacza wypożyczenie egzemplarza ksiazki przez
czytelnika (można wypożyczyć tylko jeden egzemplarz tej samej
książki; przyjmij też, że domyślnie można wypożyczyć maksymalnie 3
egzemplarze różnych książek). Akcja może być zapisana jako:<br>
("wypozycz", "Jakub Dzikowski", "Quo Vadis")<br>
    - oddaj – oznacza zwrócenie konkretnego egzemplarza książki do
biblioteki. Może być zapisane jako : ("oddaj", "Jakub Dzikowski", "Quo
Vadis")

### Przykładowe wejście:
12<br>
("dodaj", "Pan Tadeusz", "Adam Mickiewicz", 2000)<br>
("dodaj", "Quo Vadis", "Henryk Sienkiewicz", 2010)<br>
("dodaj", "Chatka Puchatka", "Alan Alexander Milne", 1998)<br>
("dodaj", "Pan Tadeusz", "Adam Mickiewicz", 2000)<br>
("dodaj", "Chatka Puchatka", " Alan Alexander Milne", 2014)<br>
("wypozycz", "Bartek Perkowski", "Pan Tadeusz")<br>
("wypozycz", "Bartek Perkowski", "Pan Tadeusz")<br>
("wypozycz", "Jacek Malyszko", "Quo Vadis")<br>
("wypozycz", "Bartek Perkowski", "Quo Vadis")<br>
("oddaj", "Jacek Malyszko", "Quo Vadis")<br>
("wypozycz", "Bartek Perkowski", "Quo Vadis")<br>
("oddaj", "Jacek Malyszko", "Quo Vadis")<br>