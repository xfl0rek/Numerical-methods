import funkcje as f
from decimal import Decimal as d


def sieczne(a, b, rodzaj, epsilon, max_iter, ktory_warunek):
    if d(f.wartosc_funkcji(rodzaj, a)) * d(f.wartosc_funkcji(rodzaj, b)) < d(0) and f.zerowanie_pochodnej(a, b, rodzaj):
        iteracja = 1
        c = d(0)
        while warunek(ktory_warunek, a, b, c, rodzaj) >= d(epsilon) and iteracja <= max_iter:
            if f.wartosc_funkcji(rodzaj, b) - f.wartosc_funkcji(rodzaj, a) == 0:
                print("Niemożliwe jest dzielenie przez 0.")
                return None
            c = d((d(b) - (f.wartosc_funkcji(rodzaj, b) * (d(b) - d(a))) / (f.wartosc_funkcji(rodzaj, b) - f.wartosc_funkcji(rodzaj, a))))

            a, b = b, c

            if a == b:
                print(f"Metoda siecznych znalazła miejsce zerowe: {c} po {iteracja} iteracjach.")
                return c

            iteracja += 1
        print(f"Metoda siecznych znalazła miejsce zerowe: {c} po {iteracja} iteracjach.")
        return c


def warunek(ktory_warunek, a, b, c, rodzaj):
    if ktory_warunek == '1':
        return d(abs(d(b) - d(a)))
    elif ktory_warunek == '2':
        return d(abs(f.wartosc_funkcji(rodzaj, c)))
    elif ktory_warunek == '3':
        return d(1)
