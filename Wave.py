import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# Clean up old frames
for name in glob.glob('tmp_{}.png'):
    os.remove(name)


def wave_packet(x, t):
    return np.exp(-(x - 3 * t) ** 2) * np.sin(3 * np.pi * (x - t))

x = np.linspace(-10, 10, 1001)

counter = 0
for t in np.linspace(-2, 2, 61):
    y = wave_packet(x, t)
    plt.plot(x, y)
    plt.axis=[x[0], x[-1], -1, 1]
    plt.xlabel('x')
    plt.ylabel('Amplitude')
    plt.savefig('tmp_{:0>4}.png'.format(counter))
    counter += 1

