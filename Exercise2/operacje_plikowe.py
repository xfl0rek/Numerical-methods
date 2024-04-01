import numpy as np


def wczytaj_macierz(sciezka):
    macierz = []
    ostatnia_kolumna = []
    with open(sciezka, 'r') as plik:
        for linia in plik:
            elementy = linia.strip().split(',')
            wiersz = [float(x) for x in elementy[:-1]]
            ostatni_element = float(elementy[-1])
            macierz.append(wiersz)
            ostatnia_kolumna.append(ostatni_element)
    return np.array(macierz), np.array(ostatnia_kolumna)
