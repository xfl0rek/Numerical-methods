import funkcje as f


macierz = [[3, 3, 1], [2, 5, 7], [1, 2, 1]]
macierz2 = [[3, 3, 1, 2], [2, 5, 7, 3], [1, 2, 1, 4], [1, 2, 3, 4]]


def main():
    f.wypisz_macierz(macierz, 3)
    dupa = f.L(macierz2)
    f.wypisz_macierz(dupa, 4)
    print(dupa)


if __name__ == "__main__":
    main()
