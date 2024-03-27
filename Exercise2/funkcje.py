import numpy as np


def wypisz_macierz(macierz, rozmiar_macierzy):
    for i in range(rozmiar_macierzy):
        print(macierz[i])


def oblicz_wyznacznik(matrix):
    wyznacznik = np.linalg.det(matrix)
    return wyznacznik


def czy_diagonalnie_dominujaca(macierz):
    n = macierz.shape[0]
    for i in range(n):
        suma = np.sum(np.abs(macierz[i])) - np.abs(macierz[i][i])
        if np.abs(macierz[i][i]) <= suma:
            return False
        return True


def gaussSeidel(A, b, max_iter=None, eps=None):
    if max_iter is not None and eps is not None:
        raise RuntimeError("Warunkami stopu dla funkcji nie może być jednocześnie ilość iteracji i epsilon!")
    x = np.zeros_like(b)
    for it_count in range(1, max_iter):
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new
    return x
