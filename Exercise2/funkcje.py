import numpy as np


def wypisz_macierz(macierz, rozmiar_macierzy):
    for i in range(rozmiar_macierzy):
        print(macierz[i])


def oblicz_wyznacznik(matrix):
    wyznacznik = np.linalg.det(matrix)
    return wyznacznik
