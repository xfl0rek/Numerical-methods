import funkcje as f
from decimal import Decimal as d


def bisekcja(a, b, rodzaj, epsilon, max_iter, ktory_warunek):
    if f.wartosc_funkcji(rodzaj, a) * f.wartosc_funkcji(rodzaj, b) < 0:
        c = d(0)
        iteracja = 1
        while warunek(ktory_warunek, a, b, c, rodzaj) >= epsilon and iteracja <= max_iter:
            c = (d(a) + d(b)) / d(2)
            if f.wartosc_funkcji(rodzaj, c) == d(0):
                print(f"\nMetoda bisekcji znalazła dokładne rozwiązanie po {iteracja} iteracjach. "
                      f"\nZnalezione miejsce zerowe: {c}")
                return c
            elif f.wartosc_funkcji(rodzaj, a) * f.wartosc_funkcji(rodzaj, c) < 0:
                b = c
            else:
                a = c
            iteracja += 1
        print(f"\nMetoda bisekcji znalazła rozwiązanie po {iteracja} iteracjach."
              f"\nZnalezione miejsce zerowe: {c}")
        return c
    else:
        print("Niepoprawnie dobrany przedział. Metoda bisekcji nie powiodła się.")
        return None


def warunek(ktory_warunek, a, b, c, rodzaj):
    if ktory_warunek == '1':
        return d(abs(d(b) - d(a)))
    elif ktory_warunek == '2':
        return d(abs(f.wartosc_funkcji(rodzaj, c)))
    elif ktory_warunek == '3':
        return d(1)
