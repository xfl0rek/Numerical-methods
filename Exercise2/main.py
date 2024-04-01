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
                print("Niepoprawny wybor")
        elif wybor == "2":
            print("dupa")
        else:
            menu = False


if __name__ == "__main__":
    main()
