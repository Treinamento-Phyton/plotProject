import matplotlib.pyplot as plt
import numpy as np

Valor_medio = 1
frequencia = 2
tempo_inicial = 0.0
tempo_final = 2.0
delta_t = 0.01

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