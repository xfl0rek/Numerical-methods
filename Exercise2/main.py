import operacje_plikowe as op
import funkcje as fun


def main():
    macierz, b = op.wczytaj_macierz("j.txt")
    print(macierz)
    print()
    print(b)
    x = fun.gauss_seidel(macierz, b, None, 10, None)
    print(x)


if __name__ == "__main__":
    main()
