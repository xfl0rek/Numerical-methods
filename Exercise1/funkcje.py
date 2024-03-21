import horner
import numpy as np
from decimal import Decimal as d
import math


def wielomian(arg):
    wartosc = horner.horner([-5, 4, 1], arg, 3)
    return d(wartosc)


def trygonometryczna(arg):
    return d(2 * math.sin(4 * arg))


def wykladnicza(arg):
    return d(2 ** arg - 2)


def zlozenie_funkcji(arg):
    return d(2 ** (horner.horner([1, 2, 1], arg, 3)) - 2)


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
        return d(2 * x + 4)
    elif rodzaj == "2":
        return d(8 * np.cos(4 * x))
    elif rodzaj == "3":
        return d((2 ** x) * np.log(2))
    elif rodzaj == "4":
        return d(np.log(2)) * d(2) ** d((horner.horner([1, 2, 1], x, 3))) * d((2 * x + 2))
    else:
        print("Podano niepoprawny rodzaj funkcji.")


def zerowanie_pochodnej(a, b, rodzaj):
    x_values = np.linspace(a, b, 1000)
    for x in x_values:
        if d(pochodna(rodzaj, x)) != d(0):
            return True
    return False
