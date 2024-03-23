import funkcje as f


macierz = [[3, 3, 1], [2, 5, 7], [1, 2, 1]]
macierz2 = [[3, 3, 1, 2], [2, 5, 7, 3], [1, 2, 1, 4], [1, 2, 3, 4]]


def main():
    f.wypisz_macierz(macierz, 3)
    print()
    dupa = f.L(macierz2)
    f.wypisz_macierz(dupa, 4)
    print()
    dupa2 = f.U(macierz2)
    f.wypisz_macierz(dupa2, 4)
    print()
    dupa3 = f.D(macierz2)
    f.wypisz_macierz(dupa3, 4)


if __name__ == "__main__":
    main()
