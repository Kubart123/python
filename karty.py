from random import randint
from Ulica import Ulica

def zaplacPodatek(gracz, ulica, gracze):
    a = 0
    if gracz[3] == ulica.wlasciciel:
        print('jesteś na swojej ulicy')
    else:
        if ulica.liczbaDomkow == 0:
            a = ulica.wynajem[0]
        elif ulica.liczbaDomkow == 1:
            a = ulica.wynajem[1]
        elif ulica.liczbaDomkow == 2:
            a = ulica.wynajem[2]
        elif ulica.liczbaDomkow == 3:
            a = ulica.wynajem[3]
        elif ulica.liczbaDomkow == 4:
            a = ulica.wynajem[4]
        elif ulica.liczbaDomkow == 5:
            a = ulica.wynajem[5]
        gracz[1] -= a
    
        for g in range(len(gracze)):
            if gracze[g][3] == ulica.wlasciciel:
                gracze[g][1] += a
                print('  zaplaciles graczowi: ', gracze[g][0], 'kwote o wysokości', a)
                break



def opsluzGracza(gracz, ulica, listaUlic, ile, gracze):
    if ulica.wlasciciel == -1 and ulica.typ == 0:#czy możesz kupić ulice
        print('  Czy chcesz kupić :', ulica.opis, ' kosztuje ona: ', ulica.kosztuje, '[tak/nie]')
        inp = 0
        while True:
            inp = input('  ')
            if inp == 'tak':#czy chcesz kupić ulice
                print('  gratulacje, kupiłeś', ulica.opis)
                gracz[1] -= ulica.kosztuje
                ulica.wlasciciel = gracz[3]
                if gracz[1] <= 0:#czy jesteś bankrutem
                    print('  * jesteś bankrutem *')
                    ile -= 1
                break
            elif inp == 'nie':
                print('  nie kupiłeś tej ulicy')
                break
            else:
                print('  zły porametr, podaj go jeszcze raz')
    #elif ulica.typ == 0 and ulica.wlasciciel >= 0:
    #    zaplacPodatek
    elif ulica.typ == 1:
        kasaSpoleczna(gracz)
    elif ulica.typ == 2:
        szansa(gracz, listaUlic)
    elif ulica.wlasciciel != -1:
        zaplacPodatek(gracz, ulica, gracze)
    elif ulica.opis == 'Idzesz Do Żabki':
        gracz[2] = 10
    elif ulica.typ == 3:
        gracz[1] -= ulica.kosztuje
    return ile

def kasaSpoleczna(gracz):
    nrKarty = randint(1, 6)
    print('  Kasa Społeczna')
    if nrKarty == 1:
        print('    Opłata ze pobyt w szpitalu: 100')
        gracz[1] -= 100
    elif nrKarty == 2:
        print('    idziesz do żabki')
        gracz[2] == 10
    elif nrKarty == 3:
        print('    idz na pole start, otrzymujesz 200')
        gracz[2] = 0
    elif nrKarty == 4:
        print('    sprzedajesz akcje z zyskiem: 50')
        gracz[1] +=  50
    elif nrKarty == 5:
        print('    dziedziczysz spadek o wysokości: 100')
        gracz[1] += 100
    elif nrKarty == 6:
        print('    pomyłka banku na kożyść banku, tracisz: 200')
        gracz[1] -= 200

def szansa(gracz, listaUlic):
    nrKarty = randint(1, 5)
    print('  Szansa')
    if nrKarty == 1:
        print('    otrzymujesz: 150')
        gracz[1] += 150
    elif nrKarty == 2:
        print('    idziesz na ulicę płowicką')
        if gracz[2] < 11:
            gracz[2] = 11
        else:
            gracz[2] = 11
            gracz[1] += 200
    elif nrKarty == 3:
        print('    idziesz na dwożec zachodni')
        if gracz[2] < 5:
            gracz[2] = 5
        else:
            gracz[2] = 5
            gracz[1] += 200
    elif nrKarty == 4:
        print('    cofasz się o 3 pola')
        gracz[2] -= 3
    elif nrKarty == 5:
        ulica = listaUlic[24]
        print('    idziesz na Plac wilsona', ulica.opis)
        gracz[2] = 24
