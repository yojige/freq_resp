import numpy as np
import math
from matplotlib import pyplot as plt


def complex_K(k, h):
    return complex(k*(1.0-2.0*h**2.0), k*(2.0*h*math.sqrt(1.0-h**2.0)))


def complex_K2(k, h):
    return complex(k, 2.0*k*h)


if __name__ =="__main__":

    m1 = 100.0
    m2 = 100.0
    m3 = 100.0E6
    k1 = 20000
    k2 = 20000
    k3 = 0.00
    h1 = 0.05
    h2 = 0.05
    h3 = 0.0

    M = np.array([[m1, 0, 0],
                [0, m2, 0],
                [0, 0, m3]])

    cmp_k1 = complex_K(k1, h1)
    cmp_k2 = complex_K(k2, h2)
    cmp_k3 = complex_K(k3, h3)

    K = np.array([[cmp_k1, -cmp_k1, 0],
                [-cmp_k1, cmp_k1+cmp_k2, -cmp_k2],
                [0,-cmp_k2,cmp_k2+cmp_k3]])

    freq = np.arange(0.01, 5, 0.01)

    X = []
    for f in freq:
        omega = 2.0 * np.pi * f
        omega2 = omega**2.0
        cmp_K = K - omega2 * M
        inv_cmp_K = np.linalg.inv(cmp_K)
        #cmp_dsp = np.dot(inv_cmp_K, np.diag(M))
        cmp_dsp = np.dot(inv_cmp_K, np.array([0, 0, m3]))
        cmp_acc = -omega2 * cmp_dsp
        X.append(list(abs(cmp_acc)))

    X1 = [r[0] for r in X]
    X2 = [r[1] for r in X]
    X3 = [r[2] for r in X]
    plt.plot(freq, X1, label="Node 1")
    plt.plot(freq, X2, label="Node 2")
    plt.plot(freq, X3, label="Node 3")
    plt.title("Transfer function")
    plt.xlabel("Frequency(Hz)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()
    plt.close()    