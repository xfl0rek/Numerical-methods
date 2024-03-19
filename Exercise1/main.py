import bisekcja
import sieczne
import rysuj_funkcje


def kryterium_zatrzymania():
    print("\nWybierz kryterium zatrzymania:")
    print("1. |xi - xi-1| < ε")
    print("2. |f(xi)| < ε")
    print("3. Wykonanie określonej liczby iteracji")

    wybor_kryterium = input()

    if wybor_kryterium == "1":
        epsilon = float(input("Podaj epsilon: "))
        max_iter = 1000
        return wybor_kryterium, epsilon, max_iter
    elif wybor_kryterium == "2":
        epsilon = float(input("Podaj epsilon: "))
        max_iter = 1000
        return wybor_kryterium, epsilon, max_iter
    elif wybor_kryterium == "3":
        max_iter = int(input("Podaj maksymalną liczbę iteracji: "))
        epsilon = 0.0
        return wybor_kryterium, epsilon, max_iter


def main():
    menu = True
    while menu:
        print("1. Wielomian (x^2 + 4x - 5)")
        print("2. Funkcja trygonometryczna (2sin(4x)")
        print("3. Wykładnicza (2^x - 2)")
        print("4. Złożenie funkcji (2^(x ^ 2 + 2x + 1) - 2)")
        print("5. Koniec\n")

        wybor = input("Wybierz funkcje: ")

        if wybor == "1":
            print("Podaj lewy kraniec przedziału:")
            a = float(input())
            print("Podaj prawy kraniec przedziału:")
            b = float(input())
            wybor_kryterium, epsilon, max_iter = kryterium_zatrzymania()
            wynik = bisekcja.bisekcja(a, b, wybor, epsilon, max_iter, wybor_kryterium)
            wynik2 = sieczne.sieczne(a, b, wybor, epsilon, max_iter, wybor_kryterium)
            if wynik is not None and wynik2 is not None:
                rysuj_funkcje.rysuj_funkcje(wybor, a, b, wynik, wynik2)
        if wybor == "2":
            print("Podaj lewy kraniec przedziału:")
            a = float(input())
            print("Podaj prawy kraniec przedziału:")
            b = float(input())
            wybor_kryterium, epsilon, max_iter = kryterium_zatrzymania()
            wynik = bisekcja.bisekcja(a, b, wybor, epsilon, max_iter, wybor_kryterium)
            wynik2 = sieczne.sieczne(a, b, wybor, epsilon, max_iter, wybor_kryterium)
            if wynik is not None and wynik2 is not None:
                rysuj_funkcje.rysuj_funkcje(wybor, a, b, wynik, wynik2)
        if wybor == "3":
            print("Podaj lewy kraniec przedziału:")
            a = float(input())
            print("Podaj prawy kraniec przedziału:")
            b = float(input())
            wybor_kryterium, epsilon, max_iter = kryterium_zatrzymania()
            wynik = bisekcja.bisekcja(a, b, wybor, epsilon, max_iter, wybor_kryterium)
            wynik2 = sieczne.sieczne(a, b, wybor, epsilon, max_iter, wybor_kryterium)
            if wynik is not None and wynik2 is not None:
                rysuj_funkcje.rysuj_funkcje(wybor, a, b, wynik, wynik2)
        if wybor == "4":
            print("Podaj lewy kraniec przedziału:")
            a = float(input())
            print("Podaj prawy kraniec przedziału:")
            b = float(input())
            wybor_kryterium, epsilon, max_iter = kryterium_zatrzymania()
            wynik = bisekcja.bisekcja(a, b, wybor, epsilon, max_iter, wybor_kryterium)
            wynik2 = sieczne.sieczne(a, b, wybor, epsilon, max_iter, wybor_kryterium)
            if wynik is not None and wynik2 is not None:
                rysuj_funkcje.rysuj_funkcje(wybor, a, b, wynik, wynik2)
        if wybor == "5":
            menu = False


if __name__ == "__main__":
    main()
