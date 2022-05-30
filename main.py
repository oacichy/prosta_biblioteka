class Egzemplarz():
    def __init__ (self, tytul, autor, rok_wyd, wypozyczony):
        self.tytul = tytul
        self.autor = autor
        self.rok_wyd = rok_wyd
        self.wypozyczony = wypozyczony
    def dodaj(self, egzemplarze):
        egzemplarze.append(Egzemplarz(self.tytul, self.autor, self.rok_wyd, self.wypozyczony))
        return True
    def wypozycz(tytul, egzemplarze):
        for temp in egzemplarze: 
            if tytul == temp.tytul and temp.wypozyczony == False:
                temp.wypozyczony = True
                return True
        return False
    def oddaj(tytul, egzemplarze):
        for temp in egzemplarze:
            if tytul == temp.tytul and temp.wypozyczony == True:
                temp.wypozyczony = False
                return True
        return False


class Czytelnik():
    def __init__(self, nazwisko):
        self.nazwisko = nazwisko
    def dodaj(self, czytelnicy):
        czytelnicy.append(Czytelnik(self.nazwisko))
    def czy_ma_konto(nazwisko, czytelnicy):
        for temp in czytelnicy:
            if nazwisko == temp.nazwisko:
                return True
        return False   

class Wypozyczone():
    def __init__(self, nazwisko, tytul):
        self.nazwisko = nazwisko
        self.tytul = tytul
    def dodaj(self, wypozyczenia):
        wypozyczenia.append(Wypozyczone(self.nazwisko, self.tytul))
    def czy_wypozyczone(nazwisko, tytul, wypozyczenia):
        for temp in wypozyczenia:
            if nazwisko == temp.nazwisko and tytul == temp.tytul:
                return True
        return False
    def czy_mozna_wypozyczyc(nazwisko, wypozyczenia):
        licznik = 0
        for temp in wypozyczenia:
            if nazwisko == temp.nazwisko:
                licznik = licznik + 1
        if licznik > 2:
            return False
        else: 
            return True
    def oddaj(nazwisko, tytul, wypozyczenia):
        for temp in wypozyczenia:
            if nazwisko == temp.nazwisko and tytul == temp.tytul:
                wypozyczenia.remove(temp)
                return True
        return False

    
czytelnicy = []
egzemplarze = []
wyniki = []
wypozyczenia = []

n = input()
for i in range (int(n)):
    temp = eval(input())
    if temp[0] == "dodaj":
        dodaj = Egzemplarz.dodaj((Egzemplarz(temp[1], temp[2], temp[3], False)), egzemplarze)
        wyniki.append(dodaj)
    if temp[0] == "wypozycz":
        spr_czytelnika = Czytelnik.czy_ma_konto(temp[1], czytelnicy)
        if spr_czytelnika is False:
            Czytelnik.dodaj((Czytelnik(temp[1])), czytelnicy)
        czymoznawypozyczyc = Wypozyczone.czy_mozna_wypozyczyc(temp[1], wypozyczenia)
        if czymoznawypozyczyc is True:
            czywypozyczone = Wypozyczone.czy_wypozyczone(temp[1], temp[2], wypozyczenia)
            if czywypozyczone == False:
                wypozycz = Egzemplarz.wypozycz(temp[2], egzemplarze)
                wyniki.append(wypozycz)
                if wypozycz == True:
                    Wypozyczone.dodaj(Wypozyczone(temp[1], temp[2]), wypozyczenia)
            else:
                wyniki.append(False)
        else:
            wyniki.append(False)
    if temp[0] == "oddaj":
        czy_wypozyczone = Wypozyczone.czy_wypozyczone(temp[1], temp[2], wypozyczenia)
        if czy_wypozyczone == False:
            wyniki.append(czy_wypozyczone)
        else:
            oddaj = Wypozyczone.oddaj(temp[1], temp[2], wypozyczenia)
            Egzemplarz.oddaj(temp[2], egzemplarze)
            wyniki.append(oddaj)


for i in wyniki:
    print(i)