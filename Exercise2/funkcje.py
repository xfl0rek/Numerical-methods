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


def gauss_seidel(A, b, x0=None, max_iter=None, epsilon=None):
    global k
    if oblicz_wyznacznik(A) == 0:
        print("Uklad sprzeczny")
        return None
    if not czy_diagonalnie_dominujaca(A):
        print("Macierz nie jest diagonalnie dominujaca")
        return None
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    if max_iter is None and epsilon is None:
        raise ValueError("Musisz podać max_iter lub epsilon.")
    if max_iter is None:
        max_iter = 1000
    if epsilon is None:
        epsilon = 1e-10

    x = x0.copy()
    for k in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x_prev[i + 1:])) / A[i, i]
        if np.linalg.norm(x - x_prev) < epsilon:
            break
    print(f"Znaleziono roziwazanie po {k + 1} iteracjach.")
    return x
