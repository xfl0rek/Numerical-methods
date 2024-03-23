def wypisz_macierz(macierz, rozmiar_macierzy):
    for i in range(rozmiar_macierzy):
        print(macierz[i])


def L(macierz):
    nowa_macierz = [wiersz[:] for wiersz in macierz]
    for i in range(len(nowa_macierz)):
        for j in range(i + 1, len(nowa_macierz[i])):
            nowa_macierz[i][j] = 0
    return nowa_macierz
