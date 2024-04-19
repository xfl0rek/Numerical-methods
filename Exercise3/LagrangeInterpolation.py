class LagrangeInterpolation:
    def __init__(self, nodes, values, interpolation_function):
        self.nodes = nodes
        self.values = values
        self.interpolation_function = interpolation_function

    def interpolate(self, x):
        result = 0
        for i in range(len(self.nodes)):
            term = self.values[i]
            for j in range(len(self.nodes)):
                if i != j:
                    term *= (x - self.nodes[j]) / (self.nodes[i] - self.nodes[j])
            result += term
        return result
