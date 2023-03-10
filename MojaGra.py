from random import randint
from Ulica import Ulica
from karty import kasaSpoleczna
from karty import szansa
from karty import opsluzGracza

def kostka():
    k = (randint(1,12))
    print('  * suma oczek na kostkach to: ', k)
    return k

def wypiszGracza(gracz):
    print('Gracz nazywa się:', gracz[0], 'Chajs:', gracz[1], 'Pole', gracz[2])

def dodajGraczaDoListy(gracze, name, nr):
    gracz = [name, 1500, 0, nr]
    gracze.append(gracz)

def zakupDomkow(gracz, listaUlic, ile):
    zakupdomkow = 0
    if gracz[1] <= 0:#sprawdza czy gracz nie zbanktótował
        print('  nic już nie kupisz')
        return 0
    while True:
        print('  czy chcesz kupić domek [ tak/t | nie/n ]: ')
        zakupdomkow = input('  ')
        if zakupdomkow == 'tak' or zakupdomkow == 't':
            print('  twoje ulice:')
            for nrUlicy in range(len(listaUlic)):#wypisuje ulice
                ulica = listaUlic[nrUlicy]
                if ulica.typ == 0 and ulica.wlasciciel == gracz[3]:
                    print(f'{nrUlicy}-{ulica.opis} <-- domek na tej ulicy kosztuje {ulica.kosztuje * (ulica.liczbaDomkow + 1)}')
            print('  na której ulicy chcesz kupić domek, podaj numer z listy(-1 = anuluj)')
            ktoraulica = int(input('  '))
            if ktoraulica == -1:
                break
            ulica = listaUlic[ktoraulica]
            if ulica.wlasciciel == gracz[3]:#na której ulicu kupuje domek
                if ulica.liczbaDomkow == 5:
                    print('  masz maksymalną liczbe domków na tej ulicy')
                    print('  wybież inną ulice')
                elif ulica.liczbaDomkow == 0:
                    gracz[1] -= ulica.kosztuje * 1
                    ulica.liczbaDomkow += 1
                elif ulica.liczbaDomkow == 1:
                    gracz[1] -= ulica.kosztuje * 2
                    ulica.liczbaDomkow += 1
                elif ulica.liczbaDomkow == 2:
                    gracz[1] -= ulica.kosztuje * 3
                    ulica.liczbaDomkow += 1
                elif ulica.liczbaDomkow == 3:
                    gracz[1] -= ulica.kosztuje * 4
                    ulica.liczbaDomkow += 1
                elif ulica.liczbaDomkow == 4:
                    gracz[1] -= ulica.kosztuje * 5
                    ulica.liczbaDomkow += 1
                if gracz[1] <= 0:
                    print('  * jesteś bankrutem *')
                    ile -= 1
                print('  Pole :', ulica.opis, ' posiada już domków:' , ulica.liczbaDomkow)#wypisuje ulice
            else:
                print('  nie jesteś właścicielem tej uicy')
        elif zakupdomkow == 'nie' or zakupdomkow == 'n':
            break
        else:
            print('  możesz napisać tylko tak, t, nie i n')
            print('  sprubuj jeszcze raz')
    return ile

def wypiszGraczy():
    for i in range(len(gracze)):
        wypiszGracza(gracze[i])

czyele = randint(1, 12) * 100 #czynsz w elektorwnie i wodociągach
listaUlic = [
    Ulica('Pole startowe', -1, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Ulica Konopacka', 0, 60, [2,10, 30, 90, 160, 250]),
    Ulica('Kasa społaczna', 2, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Ulica Stalowa', 0, 60, [4, 20, 60, 180, 320, 450]),
    Ulica('Podatek Dochadowy', 3, 200, [0, 0, 0, 0, 0, 0]),
    Ulica('Dworzec Zachodni', 0, 200, [50, 100, 150, 200, 250, 300]),
    Ulica('Ulica Radzymińska', 0, 100, [6, 30, 90, 270, 400, 550]),
    Ulica('Szansa', 1, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Ulica Jagielińska', 0, 100, [6, 30, 90, 270, 400, 550]),
    Ulica('Ulica Targowa', 0, 120, [8, 40, 100, 300, 450, 600]),
    Ulica('Przerwa Na Jedzonko', -1, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Ulica Płowiecka', 0, 140, [10, 50, 150, 450, 625, 750]),
    Ulica('Elektrownia', 0, 150, [czyele, czyele, czyele, czyele, czyele, czyele]),
    Ulica('Ulica Marsa', 0, 140, [10, 50, 150, 450, 625, 750]),
    Ulica('Ulica Grochowska', 0, 160, [12, 60, 180, 500, 700, 900]),
    Ulica('Dważec Gdański', 0, 200, [50, 100, 150, 200, 250, 300]),
    Ulica('Ulica Obozowa', 0, 180, [14, 70, 200, 550, 750, 950]),
    Ulica('Kasa Społeczna', 2, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Ulica Górczewska', 0, 180, [14, 70, 200, 550, 750, 950]),
    Ulica('Ulica Wolska', 0, 200, [16, 80, 220, 600, 800, 1000]),
    Ulica('Parking', -1, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Ulica Mickiewicza', 0, 220, [18, 90, 250, 700, 875, 1050]),
    Ulica('Szansa', 1, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Ulica Słowackiego', 0, 220, [18, 90, 250, 700, 875, 1050]),
    Ulica('Plac Wilsona', 0, 240, [20, 100, 300, 750, 925, 1100]),
    Ulica('Dworzec Wschodni', 0, 200, [50, 100, 150, 200, 250, 300]),
    Ulica('Ulica Świętokrzyska', 0, 260, [22, 110, 330, 800, 975, 1150]),
    Ulica('Krakowskie Przedmieście', 0, 260,[22, 110, 330, 800, 975, 1150]),
    Ulica('Wodociągi', 0, 150, [czyele, czyele, czyele, czyele, czyele, czyele]),
    Ulica('Nowy Świat', 0, 280, [24, 120, 360, 850, 1025, 1200]),
    Ulica('Idzesz Do Żabki', -1, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Plac Trzech Krzyży', 0, 300, [26, 130, 390, 900, 1100, 1275]),
    Ulica('Ulica Maszałkowaska', 0, 300, [26, 130, 390, 900, 1100, 1275]),
    Ulica('Kasa Społeczna', 2, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Aleje Jerozolimskie', 0, 320, [28, 150, 450, 1000, 1200, 1400]),
    Ulica('Dwożec Centralny', 0, 200, [50, 100, 150, 200, 250, 300]),
    Ulica('Szansa', 1, 0, [0, 0, 0, 0, 0, 0]),
    Ulica('Ulica Belwederska', 0, 350, [35, 175, 500, 1100, 1300, 1500]),
    Ulica('Domiar Podatkowy', 3, 100, [0, 0, 0, 0, 0 ,0]),
    Ulica('Aleje Ujazdowskie', 0, 400, [50, 200, 600, 1400, 1700, 2000, ])
]
#-1 - pola na których nic się nie dzieje
#0 - ulice
#1 - szansy
#2 - kasy społeczne
#3 - pola na których tracisz chajs

#dodawanie graczy
gracze = []
while True:
    print('czy chcesz dodać', len(gracze)+1, ' gracza(tak/t | nie/n)')
    czy = input()
    if czy == 'nie' or czy == 'n':
        if len(gracze)==0:
            print('aby grać w toł gre potrzeba gracza 😉')
            continue
        else:
            break
    elif czy == 'tak' or czy == 't':
        name = input('Podaj imię gracza :')
        dodajGraczaDoListy(gracze, name, len(gracze))
    else:
        print('  możesz wprowadzić tylko:tak/t | nie/n')
        continue


liczbaGraczy = len(gracze)
kolejnyGracz = 0
ile = len(gracze)

#cała rozgrywka
while True:
    gracz = gracze[ kolejnyGracz % liczbaGraczy ]
    kolejnyGracz += 1
    if ile <= 1:
        print(gracz[0], 'wygrał!!!!!!!!!!!!!!!')
        break#koniec gry
    elif gracz[1]<=0:
        continue#gracz któryzbankrótował nie jest usuwany z listy tylko jego tura jest omijana
    else:
        print('')
        print('Teraz gra:', gracz[0], ' hajs:', gracz[1])
        gracz[2] += kostka()
        if gracz[2]>=len(listaUlic):#ten if nie pozwala wyjść poza plansze
            gracz[2] -= len(listaUlic)
            gracz[1] += 200
        ulica = listaUlic[gracz[2]] #dodatkowe zabezpieczenie zeby byc na planszy -> % len(plansza)
        print('  Jesteś na polu:', ulica.opis)
        ile = opsluzGracza(gracz, ulica, listaUlic, ile, gracze)
        ile = zakupDomkow(gracz, listaUlic, ile)
        print('Koniec tury gracza: ',gracz[0], ' hajs:', gracz[1])
        print('zostało ci', gracz[1], ' Chajsu')
        #plansza[gracz[1] % len(plansza)]
