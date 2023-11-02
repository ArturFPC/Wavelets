import numpy as np
import pywt

# sinal de exemplo
signal = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Escolhendo uma função de wavelet (por exemplo, 'haar', 'db1', 'bior1.3', etc.)
wavelet = 'haar'

# Definindo o nível de decomposição desejado
n_levels = 2

# Realizando a transformada wavelet discreta multi-nível
coeffs = pywt.wavedec(signal, wavelet, level=n_levels)

# Recuperar os coeficientes de aproximação (cA) e detalhes (cD) em cada nível
for level in range(n_levels):
    cA, cD = coeffs[level]
    print(f"Nível {level}:")
    print("Coeficientes de Aproximação (cA):")
    print(cA)
    print("\nCoeficientes de Detalhes (cD):")
    print(cD)
