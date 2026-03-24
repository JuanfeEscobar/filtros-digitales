import numpy as np
import matplotlib.pyplot as plt

# Parámetros
t = np.linspace(-1, 1, 1000)

# Señal senoidal
f = 5
senal = np.sin(2 * np.pi * f * t)

# Transformada de Fourier
fft_senal = np.fft.fft(senal)
frecuencia = np.fft.fftfreq(len(t), t[1] - t[0])

# Graficar señal en tiempo
plt.figure()
plt.plot(t, senal)
plt.title("Señal en el Dominio del Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.show()

# Graficar magnitud del espectro
plt.figure()
plt.plot(frecuencia, np.abs(fft_senal))
plt.title("Espectro de Frecuencia (Magnitud)")
plt.xlabel("Frecuencia")
plt.ylabel("Magnitud")
plt.show()