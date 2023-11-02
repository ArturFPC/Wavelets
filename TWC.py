import numpy as np
import pywt
import matplotlib.pyplot as plt

# Crie um sinal de exemplo (neste caso, uma soma de senoides)
t = np.linspace(0, 1, num=512, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t)

# Calcule a transformada wavelet contínua (CWT) do sinal
wavelet = 'morl'  # Escolha a função de wavelet (Morlet neste caso)
scales = np.arange(1, 128)  # Escolha as escalas da CWT
cwtmatr, freqs = pywt.cwt(signal, scales, wavelet)

# Plote também o sinal original para comparação
plt.figure(figsize=(10, 2))
plt.plot(t, signal)
plt.title('Sinal Original')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()

# Plote a transformada wavelet contínua
plt.figure(figsize=(10, 6))
plt.imshow(np.abs(cwtmatr), extent=[0, 1, 1, 128], cmap='inferno', aspect='auto')
plt.colorbar(label='Magnitude')
plt.title('Transformada Wavelet Contínua')
plt.xlabel('Tempo (s)')
plt.ylabel('Escala')
plt.show()