from scipy.integrate import quad


class CompositeNewtonCotes:
    def __init__(self, function):
        self.function = function

    def integrate(self, a, b, n, tolerance, max_iterations=1000):
        global result
        prev_result = None

        for _ in range(max_iterations):
            h = (b - a) / n
            result = 0
            x0 = a

            for i in range(n):
                x1 = a + i * h
                result += quad(self.function, x0, x1)[0]
                x0 = x1

            if prev_result is not None and abs(result - prev_result) < tolerance:
                break

            prev_result = result
            n *= 2

        return result
