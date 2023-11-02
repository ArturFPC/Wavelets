import pywt
import matplotlib.pyplot as plt
import numpy as np

# Sinal de exemplo
sample_rate = 1000  # Taxa de amostragem em Hz
t = np.arange(0, 1, 1 / sample_rate)  # Vetor de tempo de 0 a 1 segundo
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Função wavelet
wavelet = 'db1'

# Definindo o nível de decomposição desejado
n_levels = 3

# Realizando a decomposição da DWT
coeffs = pywt.wavedec(signal, wavelet, level=n_levels)

# Plotar o sinal original
plt.figure(figsize=(12, 8))
plt.subplot(n_levels + 2, 1, 1)
plt.plot(t, signal)
plt.title("Sinal Original")

# Plotando os coeficientes de aproximação e detalhes
plt.figure(figsize=(12, 6))
for i in range(n_levels+1):
    plt.subplot(n_levels + 1, 1, i + 1)
    plt.plot(coeffs[i])
    plt.title(f"Nível {i}")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
