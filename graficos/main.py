import matplotlib.pyplot as plt
import numpy as np


def grafico (tempo_inicial, tempo_final, delta_t, frequencia, Valor_medio):

       # Data for plotting
       t = np.arange(tempo_inicial, tempo_final, delta_t)
       s = Valor_medio + np.sin(frequencia * np.pi * t)

       #s = t*t - 3*t + 1

       fig, ax = plt.subplots()
       ax.plot(t, s)

       ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
       ax.grid()

       fig.savefig("test.png")
       plt.show()
grafico(0.0, 2.0, 0.01, 16.0, 0.0)
grafico(0.0, 2.0, 0.01, 8.0, 0.0)
grafico(0.0, 2.0, 0.01, 4.0, 0.0)
grafico(0.0, 2.0, 0.01, 2.0, 0.0)