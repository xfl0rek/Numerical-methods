class LegendrePolynomial:
    def __init__(self, degree):
        self.degree = degree

    def value(self, x):
        n = self.degree
        if n == 0:
            return 1
        elif n == 1:
            return x

        Pn_minus_1 = 1
        Pn = x

        for k in range(1, n):
            Pn_plus_1 = ((2 * k + 1) * x * Pn - k * Pn_minus_1) / (k + 1)
            Pn_minus_1 = Pn
            Pn = Pn_plus_1

        return Pn
