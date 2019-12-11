import numpy as np
import matplotlib.pyplot as plt

with open('input', 'r') as f:
    digits = [int(i) for i in f.read()]


def decode_image(image_data, height=25, width=6):
    layers = np.array(image_data).reshape((-1, width, height))
    least_zeros = layers[np.count_nonzero(layers, axis=(1, 2)).argmax()]
    print(np.count_nonzero(least_zeros == 1) * np.count_nonzero(least_zeros == 2))
    return


def display_image(image_data, height=25, width=6):
    layers = np.array(image_data).reshape((-1, width, height))
    decoded_layer = layers[0]
    for layer in layers:
        # If layer contains value of 2 replace it
        decoded_layer = np.where(decoded_layer != 2, decoded_layer, layer)
    decoded_layer = decoded_layer.reshape(width, height)
    plt.imshow(decoded_layer)
    plt.savefig('output.png')
    plt.show()
    return


decode_image(digits)
display_image(digits)
