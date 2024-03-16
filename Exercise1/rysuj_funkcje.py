import matplotlib.pyplot as plt
import numpy as np
import funkcje as f


def rysuj_funkcje(rodzaj, a, b, miejsce_zerowe_bisekcja, miejsce_zerowe_sieczna):
    global funkcja
    argumenty = np.linspace(a, b, 1000)
    wartosci = [f.wartosc_funkcji(rodzaj, x) for x in argumenty]

    if rodzaj == '1':
        funkcja = "x^2 + 4x - 5"
    elif rodzaj == '2':
        funkcja = "2sin(4x)"
    elif rodzaj == '3':
        funkcja = "2^x - 2"
    elif rodzaj == '4':
        funkcja = "sin(x^2 + 2x + 1)"

    plt.plot(argumenty, wartosci, label=funkcja)
    plt.scatter(miejsce_zerowe_bisekcja, f.wartosc_funkcji(rodzaj, miejsce_zerowe_bisekcja), color='red', marker='o',
                label="Miejsce zerowe (bisekcja)")
    plt.scatter(miejsce_zerowe_sieczna, f.wartosc_funkcji(rodzaj, miejsce_zerowe_sieczna), color='blue', marker='x',
                label="Miejsce zerowe (sieczna)")

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(funkcja)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
