import funkcje as f


def sieczne(a, b, rodzaj, epsilon, max_iter, ktory_warunek):
    if f.wartosc_funkcji(rodzaj, a) * f.wartosc_funkcji(rodzaj, b) < 0 and f.zerowanie_pochodnej(a, b, rodzaj):
        iteracja = 0
        c = 0
        while warunek(ktory_warunek, a, b, c, rodzaj) >= epsilon and iteracja < max_iter:
            if f.wartosc_funkcji(rodzaj, b) - f.wartosc_funkcji(rodzaj, a) == 0:
                print("Niemożliwe jest dzielenie przez 0.")
                return None
            c = (b - (f.wartosc_funkcji(rodzaj, b) * (b - a)) / (f.wartosc_funkcji(rodzaj, b) - f.wartosc_funkcji(rodzaj, a)))
            a, b = b, c

            if a == b:
                print(f"Znalezione miejsce zerowe: {c} po {iteracja} iteracjach.")
                return c

            iteracja += 1
        print(f"Znalezione miejsce zerowe: {c} po {iteracja} iteracjach.")
        return c


def warunek(ktory_warunek, a, b, c, rodzaj):
    if ktory_warunek == '1':
        return abs(b - a)
    elif ktory_warunek == '2':
        return abs(f.wartosc_funkcji(rodzaj, c))
    elif ktory_warunek == '3':
        return 1
