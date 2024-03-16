import horner
import numpy as np


def wielomian(arg):
    wartosc = horner.horner([-5, 4, 1], arg, 3)
    return wartosc


def trygonometryczna(arg):
    return 2 * np.sin(4 * arg)


def wykladnicza(arg):
    return 2 ** arg - 2


def zlozenie_funkcji(arg):
    return np.sin(arg ** 2 + 2 * arg + 1)


def wartosc_funkcji(rodzaj, arg):
    if rodzaj == "1":
        return wielomian(arg)
    elif rodzaj == "2":
        return trygonometryczna(arg)
    elif rodzaj == "3":
        return wykladnicza(arg)
    elif rodzaj == "4":
        return zlozenie_funkcji(arg)
    else:
        print("Podano niepoprawny rodzaj funkcji.")


def pochodna(rodzaj, x):
    if rodzaj == "1":
        return 2 * x + 4
    elif rodzaj == "2":
        return 8 * np.cos(4 * x)
    elif rodzaj == "3":
        return (2 ** x) * np.log(2)
    elif rodzaj == "4":
        return (2 * x + 2) * np.cos((x ** 2) + 2 * x + 1)
    else:
        print("Podano niepoprawny rodzaj funkcji.")


def zerowanie_pochodnej(a, b, rodzaj):
    x_values = np.linspace(a, b, 1000)
    for x in x_values:
        if pochodna(rodzaj, x) != 0:
            return True
    return False
