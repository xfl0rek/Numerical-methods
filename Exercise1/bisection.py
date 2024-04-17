import functions as f
from decimal import Decimal as d


def bisection(a, b, type, epsilon, max_iter, which_condition):
    if f.function_value(type, a) * f.function_value(type, b) < 0:
        c = d(0)
        iteration = 1
        while condition(which_condition, a, b, c, type) >= epsilon and iteration <= max_iter:
            c = (d(a) + d(b)) / d(2)
            if f.function_value(type, c) == d(0):
                print(f"\nThe bisection method found an exact solution after {iteration} iterations."
                      f"\nFound root: {c}")
                return c
            elif f.function_value(type, a) * f.function_value(type, c) < 0:
                b = c
            else:
                a = c
            iteration += 1
        print(f"\nThe bisection method found a solution after {iteration} iterations."
              f"\nFound root: {c}")
        return c
    else:
        print("Improperly chosen interval. Bisection method failed.")
        return None


def condition(which_condition, a, b, c, type):
    if which_condition == '1':
        return d(abs(d(b) - d(a)))
    elif which_condition == '2':
        return d(abs(f.function_value(type, c)))
    elif which_condition == '3':
        return d(1)
