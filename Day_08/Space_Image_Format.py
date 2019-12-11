import numpy as np

with open('input', 'r') as f:
    digits = [int(i) for i in f.read()]

layers = np.array(digits).reshape((-1, 6, 25))
least_zeros = layers[np.count_nonzero(layers, axis=(1, 2)).argmax()]
print(np.count_nonzero(least_zeros == 1) * np.count_nonzero(least_zeros == 2))

