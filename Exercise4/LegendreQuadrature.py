from scipy.special import roots_legendre


class LegendreQuadrature:
    def __init__(self, function, nodes=5):
        self.function = function
        self.degree = nodes

    def integrate(self, a, b):
        x_mapped = lambda t: (b - a) / 2 * t + (b + a) / 2

        nodes, weights = roots_legendre(self.degree)

        integral = 0
        for i in range(self.degree):
            integral += weights[i] * self.function(x_mapped(nodes[i]))

        integral *= (b - a) / 2

        return integral
