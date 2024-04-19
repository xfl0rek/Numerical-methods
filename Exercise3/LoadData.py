def load_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        nodes = []
        values = []
        for line in lines:
            node, value = map(float, line.split())
            nodes.append(node)
            values.append(value)
    return nodes, values
