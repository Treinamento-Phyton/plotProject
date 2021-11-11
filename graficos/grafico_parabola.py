import matplotlib.pyplot as plt
import numpy as np

def grafico_parabola (a, b, c):
    delta = b*b-4*a*c
    v = -b/2*a
    tempo_inicial = v - 2
    tempo_final = v + 2
    delta_t = 0.01
    if delta < 0:
        print('delta negativo')
    else:

        # Data for plotting
        t = np.arange(tempo_inicial, tempo_final, delta_t)
        s = a*t*t + b*t + c


        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='time (s)', ylabel='Y (cm)',
               title='About as simple as it gets, folks')
        ax.grid()

        fig.savefig("test.png")
        plt.show()


grafico_parabola(1, 0, -1)
