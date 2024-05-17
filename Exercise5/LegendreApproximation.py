class LegendreApproximation:
    def __init__(self, degree):
        self.n = degree

    def function_value(self, argument):
        result = 0
        for i in range((self.n + 1) // 2):
            numerator = 1
            denominator = 1
            for j in range(i):
                numerator *= (self.n - 2 * j) * (self.n - 2 * j - 1)
                denominator *= (j + 1) * (j + 1)
            coefficient = (-1) ** i * numerator / denominator
            result += coefficient * argument ** (self.n - 2 * i)
        result *= 1 / (2 ** self.n)
        return result
