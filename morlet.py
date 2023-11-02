import numpy as np
import matplotlib.pyplot as plt
import pywt

# Parâmetros da wavelet Morlet
omega0 = 6.0
t = np.linspace(-2, 2, 1000)

# Calcule a função Morlet
morlet_wavelet = np.exp(1j * omega0 * t) * np.exp(-t**2 / 2)

# Plote a forma da wavelet Morlet
plt.figure(figsize=(8, 4))
plt.plot(t, np.real(morlet_wavelet), label='Parte Real')
plt.plot(t, np.imag(morlet_wavelet), label='Parte Imaginária')
plt.title('Wavelet Morlet')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
