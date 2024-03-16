def horner(wspolczynniki, x, dlugosc):
    wynik = 0.0
    for i in range(dlugosc - 1, -1, -1):
        wynik = wynik * x + wspolczynniki[i]
    return wynik
