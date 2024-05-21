from Exercise5.CompositeNewtonCotes import CompositeNewtonCotes
from Exercise5.Functions import function_value
from Exercise5.LegendrePolynomial import LegendrePolynomial


class Approximation:
    def __init__(self, function_type, degree, a, b, epsilon, n=1):
        self.function = function_value(function_type)
        self.degree = degree
        self.a = a
        self.b = b
        self.n = n
        self.epsilon = epsilon

    def approximated_function(self, x):
        lp = LegendrePolynomial(self.degree)
        return lp.value(x) * self.function(x)

    def ApproximationCoefficients(self):
        tab = []
        for i in range(self.degree + 1):
            integrator1 = CompositeNewtonCotes(lambda x: LegendrePolynomial(i).value(x) * self.function(x))
            integrator2 = CompositeNewtonCotes(lambda x: LegendrePolynomial(i).value(x) ** 2)
            c = (integrator1.integrate(self.a, self.b, self.n, self.epsilon) /
                 integrator2.integrate(self.a, self.b, self.n, self.epsilon))
            tab.append(c)
        return tab

    def ApproximationPolynomial(self, x):
        result = 0
        tab = self.ApproximationCoefficients()
        for i in range(len(tab)):
            lp = LegendrePolynomial(i)
            result += tab[i] * lp.value(x)
        return result

    def ErrorHelper(self, x):
        return (self.function(x) - self.ApproximationPolynomial(x)) ** 2

    def ApproximationError(self):
        integrator = CompositeNewtonCotes(self.ErrorHelper)
        return integrator.integrate(self.a, self.b, self.n, self.epsilon)
