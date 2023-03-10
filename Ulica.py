class Ulica:
    opis = ''
    typ = 0 #0 - ulica, 1 - szansa, 2 - kasa spoleczna
    kosztuje = 0
    liczbaDomkow = 0
    wynajem = [0,0,0,0,0]
    wlasciciel = -1

    def __init__(self, opis, typ, kosztuje, wynajem):
        self.opis = opis
        self.typ  = typ
        self.kosztuje = kosztuje
        self.liczbaDomkow = 0
        self.wynajem = wynajem
        self.wlasciciel = -1
