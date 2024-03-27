import numpy as np
import funkcje as fun

A = np.array([[1.0, 0.2, 0.3],
              [0.1, 1.0, -0.3],
              [-0.1, -0.2, 1.0]])

b = np.array([1.5, 0.8, 0.7])

A1 = np.array([[3.0, 3.0, 1.0],
              [2.0, 5.0, 7.0],
              [1.0, 2.0, 1.0]])


def main():
    print(fun.czy_diagonalnie_dominujaca(A))
    print(fun.czy_diagonalnie_dominujaca(A1))
    if fun.czy_diagonalnie_dominujaca(A):
        wynik = fun.gauss_seidel(A, b, '1', 10, 0)
        print(wynik)


if __name__ == "__main__":
    main()
