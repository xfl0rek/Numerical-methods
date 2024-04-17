import numpy as np


def load_matrix(path):
    matrix = []
    last_column = []
    with open(path, 'r') as file:
        for line in file:
            elements = line.strip().split(',')
            row = [float(x) for x in elements[:-1]]
            last_element = float(elements[-1])
            matrix.append(row)
            last_column.append(last_element)
    return np.array(matrix), np.array(last_column)
