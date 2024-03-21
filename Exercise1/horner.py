from decimal import Decimal as d

def horner(wspolczynniki, x, dlugosc):
    wynik = d(0)
    for i in range(dlugosc - 1, -1, -1):
        wynik = wynik * d(x) + d(wspolczynniki[i])
    return d(wynik)
