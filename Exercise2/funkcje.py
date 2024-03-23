def wypisz_macierz(macierz, rozmiar_macierzy):
    for i in range(rozmiar_macierzy):
        print(macierz[i])


def L(macierz):
    nowa_macierz = [wiersz[:] for wiersz in macierz]
    for i in range(len(nowa_macierz)):
        for j in range(i + 1, len(nowa_macierz[i])):
            nowa_macierz[i][j] = 0
    return nowa_macierz


def U(macierz):
    nowa_macierz = [wiersz[:] for wiersz in macierz]
    for i in range(len(nowa_macierz)):
        for j in range(len(nowa_macierz)):
            if j < i:
                nowa_macierz[i][j] = 0
    return nowa_macierz


def D(macierz):
    nowa_macierz = [wiersz[:] for wiersz in macierz]
    _L = L(nowa_macierz)
    _U = U(_L)
    _D = _U
    return _D


def czy_dobrze_okreslona(macierz):
    wynik = 0
    for i in range(len(macierz)):
        if macierz[i][i] != 0:
            wynik += 1
    if wynik == len(macierz):
        return True
    else:
        return False
