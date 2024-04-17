from decimal import Decimal as d


def horner(coefficients, x, length):
    result = d(0)
    for i in range(length - 1, -1, -1):
        result = result * d(x) + d(coefficients[i])
    return d(result)
