import operacje_plikowe as op
import funkcje as fun


def main():
    menu = True
    while menu:
        print("1. Wczytaj z pliku")
        print("2. Podaj ilość równań")
        print("3. Koniec")
        wybor = input()
        if wybor == "1":
            print("Podaj pzykład (*.txt): ")
            przyklad = input()
            print("Wybierz kryterium zatrzymania")
            print("1. Liczba iteracji")
            print("2. Dokładność")
            wybor2 = input()

            if wybor2 == "1":
                macierz, b = op.wczytaj_macierz(przyklad)
                print("Podaj maksymalną liczbę iteracji:")
                max_iter = int(input())
                wynik = fun.gauss_seidel(macierz, b, None, max_iter, None)
                print(wynik)
            elif wybor2 == "2":
                macierz, b = op.wczytaj_macierz(przyklad)
                print("Podaj dokładność: ")
                epsilon = float(input())
                wynik = fun.gauss_seidel(macierz, b, None, None, epsilon)
                print(wynik)
            else:
                print("Niepoprawny wybór.")
        elif wybor == "2":
            print("Podaj ile równań chcesz rozwiązać:")
            ile = int(input())
            print("Wybierz kryterium zatrzymania")
            print("1. Liczba iteracji")
            print("2. Dokładność")
            wybor2 = input()

            if wybor2 == "1":
                print("Podaj maksymalna liczbe iteracji:")
                max_iter = int(input())
                wybrane_rownania = []
                wyniki = []
                for i in range(ile):
                    print(f"Podaj nazwę {i + 1} rownania:")
                    x = input()
                    wybrane_rownania.append(x)

                for i in range(len(wybrane_rownania)):
                    przyklad = wybrane_rownania[i]
                    macierz, b = op.wczytaj_macierz(przyklad)
                    wynik = fun.gauss_seidel(macierz, b, None, max_iter, None)
                    wyniki.append(wynik)
                print(wyniki)
            elif wybor2 == "2":
                print("Podaj dokładność:")
                epsilon = float(input())
                wybrane_rownania = []
                wyniki = []
                for i in range(ile):
                    print(f"Podaj nazwę {i + 1} rownania:")
                    x = input()
                    wybrane_rownania.append(x)
                for i in range(len(wybrane_rownania)):
                    przyklad = wybrane_rownania[i]
                    macierz, b = op.wczytaj_macierz(przyklad)
                    wynik = fun.gauss_seidel(macierz, b, None, None, epsilon)
                    wyniki.append(wynik)
                print(wyniki)
            else:
                print("Niepoprawny wybór.")
        else:
            menu = False


if __name__ == "__main__":
    main()
