import numpy as np
import funkcje as fun

A = np.array([[1.0, 0.2, 0.3],
              [0.1, 1.0, -0.3],
              [-0.1, -0.2, 1.0]])

b = np.array([1.5, 0.8, 0.7])


def main():
    wynik = fun.gaussSeidel(A, b, 10)
    print(wynik)


if __name__ == "__main__":
    main()
