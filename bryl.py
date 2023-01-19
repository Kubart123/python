from klassbryl import wszst


print('Co obliczasz \n 1 - objętość sześcianu \n 2 - objętość prostopadłościanu \n 3 - objętość graniastosłupa \n 4 - objętość ostrosłupa \n 5 - objętość walca \n 6 - objętość KULI \n 7 - pole sześcianu \n 8 - pole prostopadłościanu \n 9 - pole graniastosłupa \n 10 - pole ostrosłupa \n 11 - pole walca \n 12 - pole KULI')

inp = int(input())

if inp == 1:
    Ouagadougou = wszst(float(input('dej a ')),0,0,0,0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objszescian()
if inp == 2:
    Ouagadougou = wszst(float(input('dej a ')),float(input('dej b ')),float(input('dej c ')),0,0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objprostopadloscian()
if inp == 3:
    Ouagadougou = wszst(0,0,0,0,float(input('dej wysokosc ')),float(input('dej pole podstawy ')),0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objgraniastoslup()
if inp == 4:
    Ouagadougou = wszst(0,0,0,0,float(input('dej wysokosc ')),float(input('dej pole podstawy ')),0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objostroslup()
if inp == 5:
    Ouagadougou = wszst(0,0,0,float(input('dej promien ')),float(input('dej wysokosc ')),0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objwalec()
if inp == 6:
    Ouagadougou = wszst(0,0,0,float(input('dej promien ')),0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.objkula()


if inp == 7:
    Ouagadougou = wszst(float(input('dej a ')),0,0,0,0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.poleszescian()

if inp == 8:
    Ouagadougou = wszst(float(input('dej a ')),float(input('dej b ')),float(input('dej c ')),0,0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.poleprostopadloscian()

if inp == 9:
    Ouagadougou = wszst(0,0,0,0,0,float(input('dej pole podstawy ')),float(input('dej pole boków ')))
    lista = [Ouagadougou]
    for obj in lista:
        obj.polegraniastoslup()

if inp == 10:
    Ouagadougou = wszst(0,0,0,0,0,float(input('dej pole podstawy ')),float(input('dej pole boków ')))
    lista = [Ouagadougou]
    for obj in lista:
        obj.poleostroslup()

if inp == 11:
    Ouagadougou = wszst(0,0,0,float(input('dej promien ')),float(input('dej wysokosc ')),0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.polewalec()

if inp == 12:
    Ouagadougou = wszst(0,0,0,float(input('dej promien ')),0,0,0)
    lista = [Ouagadougou]
    for obj in lista:
        obj.polekula()
        
        ----------------------------------------------------------------------------------
        
        
        
        from math import pi
class wszst:


    def __init__(self,a,b,c,r,h,pp,pb):
        self.a = a
        self.b = b
        self.c = c
        self.r = r
        self.h = h
        self.pp = pp
        self.pb = pb






    def objszescian(self):
        print(self.a**3)

    def objprostopadloscian(self):
        print(self.a*self.b*self.c)

    def objgraniastoslup(self):
        print(self.pp*self.h)

    def objostroslup(self):
        print(1/3 * self.pp * self.h)

    def objwalec(self):
        print(pi*self.r**2*self.h)

    def objkula(self):
        print(4/3*pi*self.r**3)

    def poleszescian(self):
        print(6*self.a**2)

    def poleprostopadloscian(self):
        print(2*self.a*self.b+2*self.a*self.c+2*self.b*self.c)

    def polegraniastoslup(self):
        print(2*self.pp+self.pb)

    def poleostroslup(self):
        print(self.pp+self.pb)

    def polewalec(self):
        print(pi*2*self.r**2+2*pi*self.r*self.h)

    def polekula(self):
        print(4*pi*self.r**2)
        
        ---------------------------------------------------------------------------------------
        
        from klassfizyk import wszst

Ouagadougou = wszst

print('Co obliczasz \n 1 - prędkość \n 2 - drogę \n 3 - czas \n 4 - przyśpieszenie \n 5 - prędkość średnią \n 6 - wykres położenia od czasu \n 7 - przyśpieszenie średnie \n 8 - zmianę prędkości \n 9 - zmianę czasu \n 10 - deltę \n 11 - siłę tarcia \n 12 - siłę grawitacji \n 13 - opór areodynamiczny \n 14 - energię w spoczynku  \n 15 - ciśnienie \n 16 - energię kinetyczną  \n 17 - gęstość \n 18 - siła wyporu')

inp = int(input())

if inp == 1:
    Ouagadougou.s = float(input('Dej s '))
    Ouagadougou.t = float(input('Dej t '))
    print(Ouagadougou.s/Ouagadougou.t)
if inp == 2:
    Ouagadougou.t = float(input('Dej t '))
    Ouagadougou.v = float(input('Dej v '))
    print(Ouagadougou.t*Ouagadougou.v)
if inp == 3:
    Ouagadougou.s = float(input('Dej s '))
    Ouagadougou.v = float(input('Dej v '))
if inp == 4:
    Ouagadougou.v0 = float(input('Dej v0 '))
    Ouagadougou.vk = float(input('Dej vk '))
    Ouagadougou.t = float(input('Dej t '))
    print(abs(Ouagadougou.v0 - Ouagadougou.vk)/Ouagadougou.t)
if inp == 5:
    Ouagadougou.v0 = float(input('Dej v0 '))
    Ouagadougou.vk = float(input('Dej vk '))
    Ouagadougou.t0 = float(input('Dej t0 '))
    Ouagadougou.tk = float(input('Dej tk '))
    print((Ouagadougou.v0 + Ouagadougou.vk)/(Ouagadougou.t0 - Ouagadougou.tk))
if inp == 6:
    Ouagadougou.x0 = float(input('Dej x0 '))
    Ouagadougou.v = float(input('Dej v '))
    Ouagadougou.t = float(input('Dej t '))
    print(Ouagadougou.x0 + Ouagadougou.v * Ouagadougou.t)
if inp == 7:
    Ouagadougou.v0 = float(input('Dej v0 '))
    Ouagadougou.vk = float(input('Dej vk '))
    Ouagadougou.t0 = float(input('Dej t0 '))
    Ouagadougou.tk = float(input('Dej tk '))
    print((Ouagadougou.v0 + Ouagadougou.vk)/(Ouagadougou.t0 - Ouagadougou.tk))
if inp == 8:
    Ouagadougou.v0 = float(input('Dej v0 '))
    Ouagadougou.vk = float(input('Dej vk '))
    print(abs(Ouagadougou.v0-Ouagadougou.vk))
if inp == 9:
    Ouagadougou.t0 = float(input('Dej t0 '))
    Ouagadougou.tk = float(input('Dej tk '))
    print(abs(Ouagadougou.t0 - Ouagadougou.tk))
if inp == 10:
    Ouagadougou.adodelty = float(input('Dej a '))
    Ouagadougou.bdodelty = float(input('Dej b '))
    Ouagadougou.cdodelty = float(input('Dej c '))
    print(Ouagadougou.bdodelty-4*Ouagadougou.adodelty*Ouagadougou.cdodelty)
if inp == 11:
    Ouagadougou.fn = float(input('Dej fn '))
    Ouagadougou.fs = float(input('Dej fs '))
    print(Ouagadougou.fn*Ouagadougou.fs)
if inp == 12:
    Ouagadougou.m = float(input('Dej m '))
    Ouagadougou.g = float(input('Dej g '))
    print(Ouagadougou.m*Ouagadougou.g)
if inp == 13:
    Ouagadougou.p = float(input('Dej gęstość powietrza '))
    Ouagadougou.v = float(input('Dej v '))
    Ouagadougou.cd = float(input('Dej cd '))
    Ouagadougou.area = float(input('Dej powierzchnię '))
    print(Ouagadougou.p/2 * Ouagadougou.v**2 * Ouagadougou.cd * Ouagadougou.area)
if inp == 14:
    Ouagadougou.m = float(input('Dej m '))
    print(Ouagadougou.m*Ouagadougou.c**2)
if inp == 15:
    Ouagadougou.fn = float(input('Dej fn '))
    Ouagadougou.area = float(input('Dej powierzchnię '))
    print(Ouagadougou.fn/Ouagadougou.area)
if inp == 16:
    Ouagadougou.m = float(input('Dej m '))
    Ouagadougou.v = float(input('Dej v '))
    print(Ouagadougou.m/2*Ouagadougou.v**2)
if inp == 17:
    Ouagadougou.m = float(input('Dej m '))
    Ouagadougou.objetosc = float(input('Dej objętość '))
    print(Ouagadougou.m/Ouagadougou.objetosc)
if inp == 18:
    Ouagadougou.dc = float(input('Dej gęstość cieczy'))
    Ouagadougou.objetosc = float(input('Dej objętość '))
    Ouagadougou.g = float(input('Dej g '))
    print(Ouagadougou.dc*Ouagadougou.objetosc*Ouagadougou.g)

---------------------------------------------------------------------------------------------

class wszst:


    def __init__(self,v,s,t,v0,vk,s0,t0,sk,tk,a,vsr,x0,xt,asr,deltav,deltat,adodelty,bdodelty,cdodelty,fn,fs,m,g,p,cd,area,c,objetosc,dc):
        self.s = s
        self.v = v
        self.t = t
        self.v0 = v0
        self.vk = vk
        self.s0 = s0
        self.t0 = t0
        self.sk = sk
        self.tk = tk
        self.a = a
        self.vsr = vsr
        self.x0 = x0
        self.xt = xt
        self.asr = asr
        self.deltav = deltav
        self.deltat = deltat
        self.adodelty = adodelty
        self.bdodelty = bdodelty
        self.cdodelty = cdodelty
        self.fn = fn
        self.fs = fs
        self.m = m
        self.g = g
        self.p = p
        self.cd = cd
        self.area = area
        self.c = c
        self.objetosc = objetosc
        self.dc = dc





    def kalkulujv(self):
        print(self.s / self.t)
    def kalkulujs(self):
        print(self.t * self.v)
    def kalkulujt(self):
        print(self.s / self.v)
    def kalkuluja(self):
        print(abs(self.v0 - self.vk)/self.t)
    def kalkulujvsr(self):
        print((self.v0 + self.vk)/(self.t0 - self.tk))
    def kalkulujxt(self):
        print(self.x0 + self.v * self.t)
    def kalkulujasr(self):
        print(abs(self.v0 - self.vk) / (self.t0 - self.tk))
    def kalkulujdeltav(self):
        print(abs(self.v0-self.vk))
    def kalkulujdeltat(self):
        print(abs(self.t0-self.tk))
    def kalkulujdelte(self):
        print(self.bdodelty-4*self.adodelty*self.cdodelty)
    def kalkulujft(self):
        print(self.fn*self.fs)
    def kalkulujfg(self):
        print(self.m*self.g)
    def kalkulujopor(self):
        print(self.p/2 * self.v**2 * self.cd * self.area)
    def kalkulujajnstajn(self):
        print(self.m*self.c**2)
    def kalkulujprawopascala(self):
        print(self.fn/self.area)
    def kalkulujpewpew(self):
        print(self.m/2*self.v**2)
    def kalkulujgestosc(self):
        print(self.m/self.objetosc)
    def kalkulujwypornosc(self):
        print(self.dc*self.objetosc*self.g)
        
        -----------------------------------------------------------------------------
        
        class wszst:


    s = float(0)
    v = float(0)
    t = float(0)
    v0 = float(0)
    vk = float(0)
    s0 = float(0)
    t0 = float(0)
    sk = float(0)
    tk = float(0)
    a = float(0)
    vsr = float(0)
    x0 = float(0)
    xt = float(0)
    asr = float(0)
    deltav = float(0)
    deltat = float(0)
    adodelty = float(0)
    bdodelty = float(0)
    cdodelty = float(0)
    fn = float(0)
    fs = float(0)
    m = float(0)
    g = float(0)
    p = float(0)
    cd = float(0)
    area = float(0)
    c = float(299792458)
    objetosc = float(0)
    dc = float(0)
