import functions as f
from decimal import Decimal as d


def secant(a, b, type, epsilon, max_iter, which_condition):
    if d(f.function_value(type, a)) * d(f.function_value(type, b)) < d(0) and f.find_derivative_zero(a, b, type):
        iteration = 1
        c = d(0)
        while condition(which_condition, a, b, c, type) >= d(epsilon) and iteration <= max_iter:
            if f.function_value(type, b) - f.function_value(type, a) == 0:
                print("Division by zero is not possible.")
                return None
            c = d((d(b) - (f.function_value(type, b) * (d(b) - d(a))) / (f.function_value(type, b) - f.function_value(type, a))))

            a, b = b, c

            if a == b:
                print(f"The secant method found a root: {c} after {iteration} iterations.")
                return c

            iteration += 1
        print(f"The secant method found a root: {c} after {iteration} iterations.")
        return c


def condition(which_condition, a, b, c, type):
    if which_condition == '1':
        return d(abs(d(b) - d(a)))
    elif which_condition == '2':
        return d(abs(f.function_value(type, c)))
    elif which_condition == '3':
        return d(1)
